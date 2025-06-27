from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu(lang="fa"):
    if lang == "en":
        return ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton("🎛 Get Free Server"),
            KeyboardButton("💠 Referral Link"),
            KeyboardButton("📤 Donate Server"),
            KeyboardButton("📩 Contact Support")
        )
    else:
        return ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton("🎛 دریافت سرور رایگان"),
            KeyboardButton("💠 دریافت لینک رفرال"),
            KeyboardButton("📤 اهدا سرور"),
            KeyboardButton("📩 تماس با پشتیبانی")
        )