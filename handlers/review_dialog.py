from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

review_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    contact = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()

@review_router.callback_query(F.data == "review")
async def start_feedback(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Как вас зовут?")
    await state.set_state(RestourantReview.name)


@review_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Ваш номер телефона или инстаграм?")
    await state.set_state(RestourantReview.contact)


@review_router.message(RestourantReview.contact)
async def process_contact(message: types.Message, state: FSMContext):
    contact = message.text
    await state.update_data(contact=contact)
    await message.answer("Как оцениваете качество еды? (1 - плохо, 5 - отлично)")
    await state.set_state(RestourantReview.food_rating)


@review_router.message(RestourantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    food_rating = message.text
    await state.update_data(food_rating=food_rating)
    await message.answer("Как оцениваете чистоту заведения? (1 - плохо, 5 - отлично)")
    await state.set_state(RestourantReview.cleanliness_rating)


@review_router.message(RestourantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    cleanliness_rating = message.text
    await state.update_data(cleanliness_rating=cleanliness_rating)
    await message.answer("Дополнительные комментарии или жалобы:")
    await state.set_state(RestourantReview.extra_comments)


@review_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    extra_comments = message.text
    data = await state.get_data()
    summary = (
        f"Спасибо за ваш отзыв!\n"
        f"Имя: {data.get('name')}\n"
        f"Контакт: {data.get('contact')}\n"
        f"Оценка еды: {data.get('food_rating')}\n"
        f"Оценка чистоты: {data.get('cleanliness_rating')}\n"
        f"Дополнительные комментарии: {extra_comments}"
    )
    await message.answer(summary)
    await state.clear()

