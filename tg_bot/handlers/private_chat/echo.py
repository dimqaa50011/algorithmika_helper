from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.dispatcher.storage import FSMContext


async def echo_text(message: Message, state: FSMContext):
    if await state.get_state() is None:
        msg = '___Это без состояния___\n{}'.format(message.text)
    else:
        msg = '___Это c состоянием___\n{}'.format(message.text)
    await message.answer(msg)


def register_echo_handler(dp: Dispatcher):
    dp.register_message_handler(echo_text, state='*')
