from typing import List, Any, AsyncIterable

from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from services.api_client.course_client import CourseClient
from services.api_client.student_client import StudentClient
from schemas.course import OutCourseSchema
from schemas.student import OutStudentSchema
from schemas.menu_callback_data import CreateMenuCallback


menu_callback = CallbackData('menu', 'level', 'report', 'course_id', 'student_id')

async def make_callback_data(params: CreateMenuCallback):
    return menu_callback.new(
        level=params.level,
        report=params.report,
        course_id=params.course_id,
        student_id=params.student_id
    )


async def get_main_manu_markup():
    CURRENT_LEVEL = 0


    markup = InlineKeyboardMarkup(row_width=3)
    markup.insert(
        InlineKeyboardButton(
            text='Отметить посещаемость',
            callback_data=await make_callback_data(CreateMenuCallback(level=CURRENT_LEVEL + 1))
        )
    )
    markup.insert(
        InlineKeyboardButton(
            text='Предоставить отчет',
            callback_data=await make_callback_data(CreateMenuCallback(level=CURRENT_LEVEL + 1, report=1))
        )
    )

    return markup


async def get_groups_markup():
    CURRENT_LEVEL = 1
    course_client = CourseClient()

    markup = InlineKeyboardMarkup(row_width=1)
    courses = await course_client.get_all_items()

    async for course in _async_iterator(courses.courses):
        course: OutCourseSchema
        callback = await make_callback_data(
            CreateMenuCallback(
                level=CURRENT_LEVEL + 1,
                course_id=course.id
            )
        )
        markup.insert(
            InlineKeyboardButton(
                text=f'{course.title} {course.start_date} {course.start_time}',
                callback_data=callback
            )
        )
    
    back_callback = await make_callback_data(
        CreateMenuCallback(level=CURRENT_LEVEL - 1)
    )
    markup.row(InlineKeyboardButton(text='Назад', callback_data=back_callback))
    return markup


async def get_students_markup(course_id: int):
    student_client = StudentClient()
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup(row_width=1)
    students = await student_client.get_students_by_course(course_id)

    async for student in _async_iterator(students.students):
        student: OutStudentSchema
        callback = await make_callback_data(
            CreateMenuCallback(
                level=CURRENT_LEVEL + 1,
                course_id=course_id,
                student_id=student.id
            )
        )

        markup.insert(
            InlineKeyboardButton(
                text=f'{student.first_name} {student.last_name}',
                callback_data=callback
            )
        )
    back_callback = await make_callback_data(
        CreateMenuCallback(level=CURRENT_LEVEL - 1)
    )
    markup.row(InlineKeyboardButton(text='Назад', callback_data=back_callback))
    return markup


async def _async_iterator(data: List[Any]) -> AsyncIterable:
    for item in data:
        yield item

