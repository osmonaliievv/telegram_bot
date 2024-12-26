from aiogram import Router, F, types
from aiogram.fsm.state import StatesGroup, State, default_state
from aiogram.fsm.context import FSMContext

from bot_config import database

review_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    contact = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


def validate_name(name: str) -> bool:
    return 1 <= len(name) <= 50


def validate_rating(rating: str) -> bool:
    try:
        rating = int(rating)
        return 1 <= rating <= 5
    except ValueError:
        return False


@review_router.callback_query(F.data == "review", default_state)
async def start_feedback(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Как вас зовут?")
    await state.set_state(RestourantReview.name)


@review_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    if not validate_name(name):
        await message.answer("Имя должно быть от 1 до 50 символов.")
        return
    await state.update_data(name=name)
    await message.answer("Ваш номер телефона?")
    await state.set_state(RestourantReview.contact)


@review_router.message(RestourantReview.contact)
async def process_contact(message: types.Message, state: FSMContext):
    contact = message.text
    kb = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text=str(i)) for i in range(1, 6)]],
        resize_keyboard=True,
        input_field_placeholder="Оставьте оценку"
    )
    await state.update_data(contact=contact)
    await message.answer("Как оцениваете качество еды? (1 - плохо, 5 - отлично)", reply_markup=kb)
    await state.set_state(RestourantReview.food_rating)


@review_router.message(RestourantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    food_rating = message.text
    if not validate_rating(food_rating):
        await message.answer("Оценка должна быть от 1 до 5.")
        return
    kb = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text=str(i)) for i in range(1, 6)]],
        resize_keyboard=True,
        input_field_placeholder="Оставьте оценку"
    )
    await state.update_data(food_rating=food_rating)
    await message.answer("Как оцениваете чистоту заведения? (1 - плохо, 5 - отлично)", reply_markup=kb)
    await state.set_state(RestourantReview.cleanliness_rating)


@review_router.message(RestourantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    cleanliness_rating = message.text
    if not validate_rating(cleanliness_rating):
        await message.answer("Оценка должна быть от 1 до 5.")
        return
    kb = types.ReplyKeyboardRemove()
    await state.update_data(cleanliness_rating=cleanliness_rating)
    await message.answer("Дополнительные комментарии или жалобы:", reply_markup=kb)
    await state.set_state(RestourantReview.extra_comments)


@review_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    extra_comments = message.text
    await state.update_data(extra_comments=extra_comments)
    data = await state.get_data()
    summary = (
        f"Спасибо за ваш отзыв!\n"
        f"Имя: {data.get('name')}\n"
        f"Контакт: {data.get('contact')}\n"
        f"Оценка еды: {data.get('food_rating')}\n"
        f"Оценка чистоты: {data.get('cleanliness_rating')}\n"
        f"Дополнительные комментарии: {data.get('extra_comments')}"
    )
    await message.answer(summary)
    try:
        database.save_survey(data)
        await message.answer("Ваш отзыв сохранён!")
    except Exception as e:
        await message.answer(f"Ошибка сохранения отзыва: {e}")
    await state.clear()
