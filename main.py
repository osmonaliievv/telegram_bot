import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values
import logging

from handlers.other_massages import echo_router
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random import randomfile
from handlers.dialog import opros_router

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()

async def main():
    # регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(randomfile)
    dp.include_router(opros_router)
    # в самом конце
    dp.include_router(echo_router)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())