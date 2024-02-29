from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.media_group import MediaGroupBuilder

from admin.admin_inline_kb import admin_panel
from database.admin_db import AdminDB


admin_db = AdminDB()
router_admin = Router()

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
    admin_db.add(photo=photo, photo1=photo_1, photo2=photo_2, photo3=photo_3,\
                 change=change, price=price)
    
    await state.clear()


#####################  state Inline Dashboard ####################


# @router_admin.callback_query(StateFilter(None), F.data.lower() == "add")
# async def admin_add_photo(callback: CallbackQuery, state: FSMContext):
#     await callback.message.answer(text="✅Загрузите фотографии от 2 шт.",\
#                                   reply_markup=ReplyKeyboardRemove())
#     await state.set_state(Add.add_photo)


# @router_admin.callback_query(Add.add_photo, F.photo)
# async def admin_add_price(callback: CallbackQuery, state: FSMContext):
#     await callback.message.answer(text="Фотографии добавлены")
#     await state.update_data(add_photo=callback.message.text)

#     await callback.message.answer(text="✅Добавьте описание товара")
#     await state.set_state(Add.add_change)


# @router_admin.callback_query(Add.add_change, F.text)
# async def add(callback: CallbackQuery, state: FSMContext):
#     await callback.message.answer(text="Фотографии добавлены")
#     await state.update_data(add_change=callback.message.text)

#     await callback.message.answer(text="✅Укажите цену")
#     await state.set_state(Add.add_price)


# @router_admin.callback_query(Add.add_price, F.text)
# async def add(callback: CallbackQuery, state: FSMContext):
#     await state.update_data(add_price=callback.message.text)
#     await callback.message.answer(text="Цена добавлена",\
#                                   reply_markup=admin_panel())
#     list_product = await state.get_data()
#     await callback.message.answer(str(list_product))
#     await state.clear()

##################

# @router_admin.callback_query(F.data.lower() == "change")
# async def add(callback: CallbackQuery):
#     await callback.message.edit_text(text="Выберите действие",\
#                                   reply_markup=admin_panel_change())
    

# @router_admin.callback_query(F.data.lower() == "cancel")
# async def add(callback: CallbackQuery):
#     await callback.message.answer(text="Выберите действие",\
#                                 reply_markup=menu_main)
    

################## button add #######################

# @router_admin.callback_query(F.data.lower() == "add_photo")
# async def add(callback: CallbackQuery):
#     await callback.message.edit_text(text="Photo", reply_markup=admin_panel())


# @router_admin.callback_query(F.data.lower() == "add_change")
# async def add(callback: CallbackQuery):
#     await callback.message.edit_text(text="Введите в текстовое поле 👇 описание изделия", reply_markup=admin_panel())


# @router_admin.callback_query(F.data.lower() == "add_price")
# async def add(callback: CallbackQuery):
#     await callback.message.edit_text(text="price", reply_markup=admin_panel())
    

# @router_admin.callback_query(F.data.lower() == "add_cancel")
# async def add(callback: CallbackQuery):
#     await callback.message.edit_text(text=(f"Вы {callback.from_user.full_name} в админ панели"),\
#                                 reply_markup=admin_panel())
    


#################### button change #####################
    
# @router_admin.callback_query(F.data.lower() == "change_photo")
# async def change(callback: CallbackQuery):
#     await callback.message.edit_text(text="Photo change", reply_markup=admin_panel())


# @router_admin.callback_query(F.data.lower() == "change_change")
# async def change(callback: CallbackQuery):
#     await callback.message.edit_text(text="description change", reply_markup=admin_panel())
    

# @router_admin.callback_query(F.data.lower() == "change_price")
# async def change(callback: CallbackQuery):
#     await callback.message.edit_text(text="price change", reply_markup=admin_panel())


# @router_admin.callback_query(F.data.lower() == "change_cancel")
# async def change(callback: CallbackQuery):
#     await callback.message.edit_text(text=(f"Вы {callback.from_user.full_name} в админ панели"),\
#                                 reply_markup=admin_panel())