from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery, InlineKeyboardButton
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.admin_db import AdminDB

prod_db = AdminDB()
product_router = Router()


# @product_router.callback_query(F.photo)
# async def photo_showcase(callback: CallbackQuery):
#     showcase = prod_db.photo_showcase()
#     await callback.message.answer_photo(photo=showcase)


def inline_photo_showcase():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🔎ОПИСАНИЕ", callback_data="showcase")
    ), builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

@product_router.message(F.text.lower() == "/ok")
async def output_photo(message: Message):
    album = MediaGroupBuilder()
    photoss = []
    res = prod_db.photo_output()
    for photos in res:
        photoss.append(photos)
    for i in photoss:
        album.add(type="photo", media=i)
    await message.answer_media_group(media=album.build())