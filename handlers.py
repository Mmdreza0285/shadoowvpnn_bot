from aiogram import types, Dispatcher
from keyboards import get_main_menu

async def start(message: types.Message):
    lang = message.from_user.language_code
    menu = get_main_menu(lang)
    await message.answer("زبان به صورت خودکار شناسایی شد" if lang != "fa" else "زبان شما: فارسی", reply_markup=menu)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])