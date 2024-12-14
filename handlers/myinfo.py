from aiogram import Router, types
from aiogram.filters import Command

myinfo_router = Router()

@myinfo_router.message(Command("myinfo"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    id = message.from_user.id
    useer = message.from_user.username
    await message.answer(
        f"Имя, {name}! \n"
        f" id : {id} \n "
        f"Ваш ник : {useer} \n")