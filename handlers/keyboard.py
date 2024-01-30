from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


builder = ReplyKeyboardBuilder()


def menu_main():
    builder.row(
        KeyboardButton(text="ИЗДЕЛИЯ"),
        KeyboardButton(text="О НАС")
    ) 
    return builder.as_markup(resize_keyboard=True)


menu_main = menu_main()