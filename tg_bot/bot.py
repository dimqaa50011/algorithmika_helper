import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from loguru import logger

from config import BOT_TOKEN, USE_REDIS

from handlers.private_chat import register_private_handlers


def register_all_middlewares(dp: Dispatcher):
    pass


def register_all_filters(dp: Dispatcher):
    pass
    
    
def register_all_handlers(dp: Dispatcher):
    register_private_handlers(dp)


async def on_startup():
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    storage = RedisStorage2() if USE_REDIS else MemoryStorage()
    dp = Dispatcher(bot=bot, storage=storage)
    
    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)
    
    bot_session = await bot.get_session()
    
    logger.info('Bot started!!')
    
    try:
        await dp.start_polling()
    finally:
        await storage.close()
        await storage.wait_closed()
        await bot_session.close()


if __name__ == '__main__':
    try:
        asyncio.run(on_startup())
    except (SystemError, KeyboardInterrupt) as ex:
        logger.info('Bot stopped!')
