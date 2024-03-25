from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from database.admin_db import admin_db
from handlers.keyboard import menu_main


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

################## admin_panel_exit #######################

@router_admin.message(F.text == "выход")
async def exit_admin(message: Message):
    await message.answer(text="Выход из админ панели", reply_markup=menu_main)

################## admin_panel #######################
class Add(StatesGroup):
    add_photo = State()
    add_photo_1 = State()
    add_photo_2 = State()
    add_photo_3 = State()
    add_change = State()
    add_price = State()


# class DeleteProduct(StatesGroup):
#     del_product = State()


################## state add #######################

@router_admin.message(F.text == "добавить")
async def add(message: Message, state: FSMContext):
    await message.answer(text="❗Нужно загрузить 4 фото изделия❗")
    await message.answer(text="✅Загрузите лучшее первое фото (для витрины)❕",\
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(Add.add_photo)


@router_admin.message(Add.add_photo)
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

################## admin_panel_delete #######################

class DeleteProduct(StatesGroup):
    del_product = State()


@router_admin.message(F.text == "удалить")
async def delete_product(message: Message, state: FSMContext):
    await message.answer(text="Введите артикул изделия")
    await state.set_state(DeleteProduct.del_product)


@router_admin.message(DeleteProduct.del_product, F.text)
async def input_del_product(message: Message, state: FSMContext):
    text_artic = message.text.replace(" ", "")
    if text_artic.isalpha() == False:
        await state.update_data(delete_product=message.text)
        await message.answer(text="Изделие удалено",\
                                    reply_markup=admin_panel())
        del_product = await state.get_data()
        delete_prod = list(map(int, del_product.values())).pop()
        admin_db.product_delete(delete_prod)
        await state.clear()
    else:
        await message.answer("Ввод не верен !")


@router_admin.message()
async def trash_message(message: Message):
    await message.answer(text="Такой команды нет",\
                                    reply_markup=menu_main)