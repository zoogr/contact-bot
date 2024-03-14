import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode


from handlers.user_private import user_private_router

TOKEN = "тут должен быть токен"
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)

dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
