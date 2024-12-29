from aiogram import Router, F
from .start import start_router
from .menu_management import menu_management_router
from .dishes import menu_list_router
from .review_dialog import review_router
from .myinfo import myinfo_router
from .random import randomfile
from .dialog import opros_router
from .other_massages import echo_router

private_router = Router()

private_router.include_router(start_router)
private_router.include_router(myinfo_router)
private_router.include_router(randomfile)
private_router.include_router(opros_router)
private_router.include_router(review_router)
private_router.include_router(menu_management_router)
private_router.include_router(menu_list_router)
private_router.include_router(echo_router)

private_router.message.filter(F.chat.type == 'private')
private_router.callback_query.filter(F.chat.type == 'private')
