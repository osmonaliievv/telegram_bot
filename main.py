import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
import random

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(
        f"Привет, {name}! \n"
        f" Наш бот обслуживает уже 12 пользователей \n "
        f"Мои команды: \n"
        f"/start - начать работу с ботом \n"
        f"/random - случайное имя \n"
        f" /myinfo - информация о пользователе")


@dp.message(Command("myinfo"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    id = message.from_user.id
    useer = message.from_user.username
    await message.answer(
        f"Имя, {name}! \n"
        f" id : {id} \n "
        f"Ваш ник : {useer} \n")


@dp.message(Command("random"))
async def random_handler(message: types.Message):
    random_name = [
        "Александр",
        "Мария",
        "Дмитрий",
        "Анна",
        "Сергей",
        "Екатерина",
        "Иван",
        "Ольга",
        "Максим",
        "Юлия"
    ]
    selected_name = random.choice(random_name)
    await message.answer(f"Случайное имя: {selected_name}")


@dp.message()
async def echo_handler(message: types.Message):
    txt = message.text
    await message.answer(txt)


async def main():
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
