from typing import Union, Optional

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from schemas.menu_callback_data import OutMenuCallback
from schemas.student import OutStudentSchema, UpdateStudentSchema
from services.api_client.student_client import StudentClient
from keyboards.inlile.menu import (
    menu_callback,
    get_main_manu_markup,
    get_groups_markup,
    get_students_markup
)


async def show_menu(message: Union[Message, CallbackQuery], **kwargs):
    markup = await get_main_manu_markup()
    if isinstance(message, Message):
        await message.answer('Меню', reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        call = message
        await call.answer(cache_time=60)
        await call.message.edit_text('Меню')
        await call.message.edit_reply_markup(markup)



async def get_group_list(call: CallbackQuery, **kwargs):
    await call.answer(cache_time=10)
    markup = await get_groups_markup()
    await call.message.edit_text('Выбери группу')
    await call.message.edit_reply_markup(markup)


async def get_report():
    ...


async def get_student_list(call: CallbackQuery, callback_item: OutMenuCallback):
    await call.answer(cache_time=10)
    markup = await get_students_markup(callback_item.course_id)
    await call.message.edit_text('Выбери ученика')
    await call.message.edit_reply_markup(markup)


async def update_presence(call: CallbackQuery, callback_item: OutMenuCallback):
    student_client = StudentClient()
    student = await student_client.get_item(int(callback_item.student_id))
    student.is_presence = True
    await student_client.update_item(
        pk=student.id,
        data=UpdateStudentSchema(**student.dict())
    )
    markup = await get_students_markup(student.course)
    await call.message.d
    await call.message.edit_reply_markup(markup)
    await call.answer(f'{student.first_name} посещение отмечено!', show_alert=True)

async def get_report():
    ...


async def navigator(call: CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')

    callback_item = OutMenuCallback(
        report=callback_data.get('report'),
        course_id=callback_data.get('course_id'),
        student_id=callback_data.get('student_id')
    )

    levels = {
        '0': show_menu,
        '1': {
            'report': get_report,
            'presence': get_group_list
        },
        '2': get_student_list,
        '3': update_presence
    }

    curr_func = levels.get(current_level)
    if isinstance(curr_func, dict):
        curr_func = curr_func.get('report') if callback_item.report == '1' else curr_func.get('presence')
    await curr_func(call, callback_item=callback_item)


def register_before_lesson_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(navigator, menu_callback.filter())
    dp.register_message_handler(show_menu, commands=['menu'])
