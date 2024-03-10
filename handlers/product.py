from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder

from configs import msg
from database.admin_db import admin_db
from handlers.keyboard import menu_main

product_router = Router()

###############  Keybord #################
def inline_product(k):
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text=f"🔎ОПИСАНИЕ", callback_data=f"{k}")
        ), builder.adjust(1)
    return builder.as_markup(resize_keyboard=True,
                        input_field_placeholder=msg.TEXT_CHOICE_1)


def inline_product_order():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🛒ЗАКАЗАТЬ", callback_data="description_order")
    ), builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


################ output SQLITE3 #################

# @product_router.callback_query(F.data == "description_order")
# async def description_order(callback: CallbackQuery):
#     user_id = callback.message.from_user.id
#     await callback.message.answer(text=" Вы закали ") # здесь работа с базой данных


@product_router.callback_query()
async def output_product(callback: CallbackQuery):
    album = MediaGroupBuilder()         # 4 фото для витрины из БД
    for i in admin_db.photos_db():
        i = list(i)
        num = i.pop(0)
        i = tuple(i)
        if callback.data == str(num):
            for j in i:
                album.add(type=f"photo", media=j)
                # await callback.message.answer(text="<b>👇Мини кошелёк👇</b>")
    await callback.message.answer_media_group(media=album.build())

    
    for k, v in admin_db.description_db():
        if callback.data == str(k):        # описание из БД
            await callback.message.answer(text=v)

    for k, v in admin_db.price_db():        # цена из БД
        if callback.data == str(k):
            await callback.message.answer(text=f"Цена: {v}",\
                                        reply_markup=inline_product_order())
            
# @product_router.message()
# async def trash_message(message: Message):
#     await message.answer(text="Такой команды нет",\
#                                     reply_markup=menu_main)