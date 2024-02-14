from aiogram.types import InlineKeyboardButton
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder


def admin_panel():
    builder_admin_panel = InlineKeyboardBuilder()
    builder_admin_panel.row(
        InlineKeyboardButton(text="добавить", callback_data="add"),
        InlineKeyboardButton(text="изменить", callback_data="change"),
        InlineKeyboardButton(text="выход", callback_data="cancel"),
    ), builder_admin_panel.adjust(3)
    return builder_admin_panel.as_markup(resize_keyboard=True)

################## button add ###################

def admin_panel_add():
    builder_admin_panel = InlineKeyboardBuilder()
    builder_admin_panel.row(
        InlineKeyboardButton(text="фотографии", callback_data="add_photo"),
        InlineKeyboardButton(text="описание", callback_data="add_change"),
        InlineKeyboardButton(text="цена", callback_data="add_price"),
        InlineKeyboardButton(text="нвзвд", callback_data="add_cancel"),
    ), builder_admin_panel.adjust(3, 1)
    return builder_admin_panel.as_markup(resize_keyboard=True)

################# if add_photo ####################


################# if add_cancel ####################






################## button change ###################

def admin_panel_change():
    builder_admin_panel = InlineKeyboardBuilder()
    builder_admin_panel.row(
        InlineKeyboardButton(text="фотографии", callback_data="change_photo"),
        InlineKeyboardButton(text="описание", callback_data="change_change"),
        InlineKeyboardButton(text="цену", callback_data="change_price"),
        InlineKeyboardButton(text="назад", callback_data="change_cancel"),
    ), builder_admin_panel.adjust(3, 1)
    return builder_admin_panel.as_markup(resize_keyboard=True)

################## button exit ###################