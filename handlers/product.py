from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder

from configs import msg
from database.admin_db import AdminDB

prod_db = AdminDB()
product_router = Router()


###############  Keybord #################
def inline_product():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🔎ОПИСАНИЕ", callback_data="description")
    ), builder.adjust(1)
    return builder.as_markup(resize_keyboard=True,
                             input_field_placeholder=msg.TEXT_CHOICE_1)

def inline_product_order():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🛒ЗАКАЗАТЬ", callback_data="description_order")
    ), builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


################## output ###################


@product_router.callback_query(F.data == "description")
async def output_product(callback: CallbackQuery):
    album = MediaGroupBuilder()
    result = prod_db.photos_db()
    for i in result:
        album.add(type="photo", media=i)
    await callback.message.answer(text="<b>👇Мини кошелёк👇</b>")
    await callback.message.answer_media_group(media=album.build())
    for j in prod_db.description_db():        
        await callback.message.answer(text=j)
    for k in prod_db.price_db():
        await callback.message.answer(text=f"Цена: {k}", reply_markup=inline_product_order())


@product_router.callback_query(F.data == "description_order")
async def description_order(callback: CallbackQuery):
    await callback.message.answer(text=" Вы закали ") # здесь работа с базой данных


# @product_router.callback_query(F.photo)
# async def photo_showcase(callback: CallbackQuery):
#     showcase = prod_db.photo_showcase()
#     await callback.message.answer_photo(photo=showcase)


# def inline_photo_showcase():
#     builder = InlineKeyboardBuilder()
#     builder.row(
#         InlineKeyboardButton(text="🔎ОПИСАНИЕ", callback_data="showcase")
#     ), builder.adjust(1)
#     return builder.as_markup(resize_keyboard=True)


@product_router.message(F.text.lower() == "/ok")
async def output_photo(message: Message):
    album = MediaGroupBuilder()
    result = prod_db.photo_output()
    for i in result:
        album.add(type="photo", media=i)
    await message.answer_media_group(media=album.build())