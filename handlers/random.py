from aiogram import Router, types
from aiogram.filters import Command
import random

randomfile = Router()


@randomfile.message(Command("random"))
async def random_handler(message: types.Message):
    random_name = ["Александр", "Мария", "Дмитрий", "Анна", "Сергей", "Екатерина", "Иван", "Ольга", "Максим", "Юлия"]
    selected_name = random.choice(random_name)
    await message.answer(f"Случайное имя: {selected_name}")
