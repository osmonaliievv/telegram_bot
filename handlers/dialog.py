from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

opros_router = Router()


class Opros(StatesGroup):
    name = State()
    age = State()
    ganre = State()


@opros_router.message(Command("opros"))

async def sart_opros(message: types.Message, state: FSMContext):
    await message.answer("Как вас зовут?")
    await state.set_state(Opros.name)


@opros_router.message(Opros.name)
async def sart_opros(message: types.Message, state: FSMContext):
    name = message.text
    await message.answer(f"{name} сколько вам лет?")
    await state.set_state(Opros.age)


@opros_router.message(Opros.age)
async def sart_opros(message: types.Message, state: FSMContext):
    await message.answer("Укажите ваш любимый жанр?")
    await state.set_state(Opros.ganre)


@opros_router.message(Opros.ganre)
async def sart_opros(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за пройденный опрос")
    await state.clear()
