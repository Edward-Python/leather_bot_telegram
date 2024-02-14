from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

from configs import msg


def menu_main():
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="👀 ИЗДЕЛИЯ"),
        KeyboardButton(text="🔎 О НАС"),
        KeyboardButton(text="🚚 УСЛОВИЯ ДОСТАВКИ")
    ), builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True,
                             input_field_placeholder=msg.TEXT_CHOICE_1)


def production_process():
    builder0 = ReplyKeyboardBuilder()
    builder0.row(
        KeyboardButton(text="🛠 ИСПОЛЬЗУЕМЫЕ ИНСТРУМЕНТЫ"),
        KeyboardButton(text="✂ ОБРАБОТКА КОЖИ"),
        KeyboardButton(text="НАЗАД")
    ), builder0.adjust(1, 1, 1)
    return builder0.as_markup(resize_keyboard=True,
                              input_field_placeholder=msg.TEXT_CHOICE_1)


menu_main = menu_main()
production_process = production_process()