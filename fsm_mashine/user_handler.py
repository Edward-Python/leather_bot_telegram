import os
from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from handlers.keyboard import menu_main
from database.user_db import user_db


router_user = Router()


def inline_product_order():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text=f"🛒ЗАКАЗАТЬ",\
                             callback_data="order")
    ), builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


class Add(StatesGroup):
    id_product = State()
    full_name = State()
    index_adress = State()
    number_phon = State()

################## state add ###################

@router_user.callback_query(StateFilter(None), F.data == "order")
async def user_order(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text="<b>Оформление заказа</b>")
    await callback.message.answer(text="Укажите Артикул товара")
    await state.set_state(Add.id_product)


@router_user.message(Add.id_product, F.text)
async def add(message: Message, state: FSMContext):
    await state.update_data(id_product=message.text)

    await message.answer(text="Введите Ф.И.О. (полные)")
    await state.set_state(Add.full_name)


@router_user.message(Add.full_name, F.text)
async def add(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)

    await message.answer(text="Укажите индекс и адрес доставки")
    await state.set_state(Add.index_adress)


@router_user.message(Add.index_adress)
async def add(message: Message, state: FSMContext):
    await state.update_data(index_adress=message.text)

    await message.answer(text="Введите номер телефона: +7")
    await state.set_state(Add.number_phon)


@router_user.message(Add.number_phon, F.text)
async def add_input(message: Message, state: FSMContext):
    await state.update_data(number_phon=message.text)
    await message.answer(text="Заказ оформлен", reply_markup=menu_main)
    dict_data_user = await state.get_data()
    list_data_user = []
    for k, v in dict_data_user.items():
        list_data_user.append(v)
    user_id = message.from_user.id
    id_product = list_data_user[0]
    full_name = list_data_user[1]
    index_adress = list_data_user[2]
    number_phon = list_data_user[3]
    user_db.add_user(id_product=id_product, user_id=user_id, full_name=full_name,\
                     index_adress=index_adress, number_phon=number_phon)
    await state.clear()
    input_order = int(os.getenv("ADMIN_ID"))
    if message.from_user.id == input_order:
        await message.answer(text=f"Заказ изделия❗")