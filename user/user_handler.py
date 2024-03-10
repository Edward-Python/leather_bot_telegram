from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message, CallbackQuery

from handlers.keyboard import menu_main
from database.user_db import user_db


router_user = Router()


class Add(StatesGroup):
    full_name = State()
    index_adress = State()
    number_phon = State()

################## state add ###################

    
@router_user.callback_query(StateFilter(None), F.data == "description_order")
async def user_order(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Оформление заказа")
    await callback.message.answer(text="Введите Ф.И.О. (полные)")
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
async def add(message: Message, state: FSMContext):
    user = message.from_user.id
    await state.update_data(number_phon=message.text)
    await message.answer(text="Заказ оформлен", reply_markup=menu_main)
    dict_data_user = await state.get_data()
    list_data_user = []
    for k, v in dict_data_user.items():
        list_data_user.append(v)
    user_id = user
    full_name = list_data_user[0]
    index_adress = list_data_user[1]
    number_phon = list_data_user[2]
    user_db.add_user(user_id=user_id, full_name=full_name,\
                     index_adress=index_adress, number_phon=number_phon)
    await state.clear()