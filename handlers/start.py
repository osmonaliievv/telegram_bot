from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="review"),
                types.InlineKeyboardButton(text="Пожертвовать", callback_data="donate"),
            ],
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://geeks.kg")
            ],
        ]
    )
    await message.answer(
        "🍴 Добро пожаловать в наш ресторан!  \n "
        "Я — ваш виртуальный помощник и помогу:\n "
        "✨ Ознакомиться с нашим меню.\n "
        "✨Доступные категории блюд:\n "
        "Супы, Салаты, Закуски, Охладительные напитки, Горячие напитки, Десерты", reply_markup=kb)
