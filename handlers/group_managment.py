from aiogram import Router, F, types

group_router = Router()
group_router.message.filter(F.chat.type != "private")

BAD_WORDS = ("дурак", "дибил")

@group_router.message(F.text)
async def check_bad_words_and_ban(message: types.Message):
    for word in BAD_WORDS:
        if word in message.text.lower():
            await message.answer(f"Пользователь {message.from_user.full_name} был забанен за использование запрещённых слов.")
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id
            )
            await message.delete()
            break
