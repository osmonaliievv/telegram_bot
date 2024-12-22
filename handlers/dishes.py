from aiogram import Router, F, types
from bot_config import database
from pprint import pprint

menu_list_router = Router()


@menu_list_router.callback_query(F.data == "menu_list")
async def show_all_menu(callback: types.CallbackQuery):
    menu_list = database.get_menu_list()
    pprint(menu_list)
    txt = ""
    for menu in menu_list:
        txt += (f"Name: {menu['food_name']}\n"
                f" Price: {menu['price']}\n"
                f" Description: {menu['description']}\n"
                f" Category: {menu['category']}\n"
                f"-------------------------------------\n")
    await callback.message.answer(txt)
