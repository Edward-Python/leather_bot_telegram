from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from database.admin_db import admin_db


router_admin = Router()

################## admin_panel #######################

def admin_panel():
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="добавить"),
        KeyboardButton(text="удалить"),
        KeyboardButton(text="выход")
    ), builder.adjust(1, 1, 1)
    return builder.as_markup(resize_keyboard=True)


################## admin_panel #######################
class Add(StatesGroup):
    add_photo = State()
    add_photo_1 = State()
    add_photo_2 = State()
    add_photo_3 = State()
    add_change = State()
    add_price = State()


################## state add #######################

@router_admin.message(StateFilter(None), F.text.lower() == "добавить")
async def add(message: Message, state: FSMContext):
    await message.answer(text="❗Нужно загрузить 4 фото изделия❗")
    await message.answer(text="✅Загрузите лучшее первое фото (для витрины)❕",\
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(Add.add_photo)


@router_admin.message(Add.add_photo, F.photo)
async def add(message: Message, state: FSMContext):    
    add_phot = message.photo[-1].file_id
    await state.update_data(add_photo=add_phot)
    await message.answer(text="Фотография добавлена")

    await state.set_state(Add.add_photo_1)
    await message.answer(text="✅Загрузите второе фото")


@router_admin.message(Add.add_photo_1, F.photo)
async def add(message: Message, state: FSMContext):    
    add_phot_1 = message.photo[-1].file_id
    await state.update_data(add_photo_1=add_phot_1)
    await message.answer(text="Фотография добавлена")

    await state.set_state(Add.add_photo_2)
    await message.answer(text="✅Загрузите третее фото")


@router_admin.message(Add.add_photo_2, F.photo)
async def add(message: Message, state: FSMContext):    
    add_phot_2 = message.photo[-1].file_id
    await state.update_data(add_photo_2=add_phot_2)
    await message.answer(text="Фотография добавлена")

    await state.set_state(Add.add_photo_3)
    await message.answer(text="✅Загрузите четвёртое фото")


@router_admin.message(Add.add_photo_3, F.photo)
async def add(message: Message, state: FSMContext):    
    add_phot_3 = message.photo[-1].file_id
    await state.update_data(add_photo_3=add_phot_3)
    await message.answer(text="Фотографии добавлены")

    await state.set_state(Add.add_change)
    await message.answer(text="✅Добавьте описание товара")


@router_admin.message(Add.add_change, F.text)
async def add(message: Message, state: FSMContext):
    await state.update_data(add_change=message.text)

    await message.answer(text="✅Укажите цену")
    await state.set_state(Add.add_price)
    

@router_admin.message(Add.add_price, F.text)
async def add(message: Message, state: FSMContext):
    await state.update_data(add_price=message.text)
    await message.answer(text="Цена добавлена",\
                                  reply_markup=admin_panel())
    list_product = await state.get_data()
    list_product = list(list_product.values())
    photo = list_product[0]
    photo_1 = list_product[1]
    photo_2 = list_product[2]
    photo_3 = list_product[3]
    change = list_product[4]
    price = list_product[5]
    admin_db.add(photo=photo, photo1=photo_1, photo2=photo_2,\
                 photo3=photo_3, change=change, price=price)
    await state.clear()