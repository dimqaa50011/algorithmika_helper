from aiogram.types import Message
from aiogram import Dispatcher

from services.api_client import UserApiClient
from schemas.user import CreateUserSchema


async def start_handler(message: Message):
    user_client = UserApiClient()
    await user_client.create_item(
        CreateUserSchema(
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            tg_username=message.from_user.username,
            tg_id=message.from_user.id
        )
    )
    await message.answer(f'Привет, {message.from_user.full_name}!')


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
