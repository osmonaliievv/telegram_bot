import asyncio
import logging
from bot_config import dp, bot, database
from handlers import private_router


async def on_startup(bot):
    database.create_tables()


async def main():
    dp.include_router(private_router)
    # регистрация роутеров
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
