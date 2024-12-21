from aiogram import Router, F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from bot_config import database
from dotenv import dotenv_values

menu_management_router = Router()

# когда создатите переменную ADMIN_ID оберните id в кавычки
menu_id = dotenv_values(".env")["ADMIN_ID"]



class Menu(StatesGroup):
    food_name = State()
    price = State()
    description = State()
    category = State()


@menu_management_router.callback_query(F.data == "menu")
async def create_menu(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id == int(menu_id):
        await callback.message.answer("Введите название блюда: ")
        await state.set_state(Menu.food_name)
    else:
        await callback.answer("У вас нет прав для добавления меню.")


@menu_management_router.message(Menu.food_name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text.strip()
    await state.update_data(food_name=name)
    await message.answer("Введите цену (число): ")
    await state.set_state(Menu.price)


@menu_management_router.message(Menu.price)
async def process_price(message: types.Message, state: FSMContext):
    try:
        price = float(message.text.strip())
        await state.update_data(price=price)
        await message.answer("Введите описание для блюда: ")
        await state.set_state(Menu.description)
    except ValueError:
        await message.answer("Пожалуйста, введите корректное число для цены.")


@menu_management_router.message(Menu.description)
async def process_description(message: types.Message, state: FSMContext):
    description = message.text.strip()
    await state.update_data(description=description)
    await message.answer("Введите категорию (супы, вторые, горячие напитки, холодные напитки и т.д.): ")
    await state.set_state(Menu.category)


@menu_management_router.message(Menu.category)
async def process_extra_comments(message: types.Message, state: FSMContext):
    category = message.text.strip()
    await state.update_data(category=category)
    data = await state.get_data()
    summary = (
        f"Спасибо за добавление блюда!\n"
        f"Название: {data.get('food_name')}\n"
        f"Цена: {data.get('price')}\n"
        f"Описание: {data.get('description')}\n"
        f"Категория: {data.get('category')}\n"
    )
    await message.answer(summary)
    try:
        print("Данные для сохранения:", data)
        database.save_menu(data)
        await message.answer("Ваше блюдо сохранено!")
    except Exception as e:
        await message.answer(f"Ошибка сохранения блюда: {e}")
    await state.clear()

