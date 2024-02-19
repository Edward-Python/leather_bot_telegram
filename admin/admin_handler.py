from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message, FSInputFile, CallbackQuery

from admin.admin_inline_kb import admin_panel_add, admin_panel_change, admin_panel
from handlers.keyboard import menu_main
from database.admin_db import AdminDB

admin_db = AdminDB()
router_admin = Router()

################## admin_panel #######################
class Add(StatesGroup):
    add_photo = State()
    add_change = State()
    add_price = State()


################## state add #######################


@router_admin.callback_query(F.data.lower() == "add")
async def add(callback: CallbackQuery):
    await callback.message.edit_text(text="Добавление информации по изделию",\
                                reply_markup=admin_panel_add())


@router_admin.callback_query(StateFilter(None), F.data.lower() == "add_photo")
async def admin_add_photo(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Add.add_photo)
    await callback.message.answer(text="✅Загрузите фотографии от 2 шт.\n\
✅Опишите изделие")
    # await admin_db.change_photo(photo=state)
    await state.clear()
    # await callback.message.answer(text="Фотографии загружены")



@router_admin.callback_query(StateFilter(None), F.data.lower() == "add_price")
async def admin_add_price(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Add.add_price)
    await callback.message.answer(text="Добавить цену изделия")
    # await admin_db.add(photo=state, price=state)
    await state.clear()
    # await admin_db.change_price(photo=state.set_state(Add.add_price))
    # await callback.message.answer(text="Цена установлена")


##################

@router_admin.callback_query(F.data.lower() == "change")
async def add(callback: CallbackQuery):
    await callback.message.edit_text(text="Выберите действие",\
                                  reply_markup=admin_panel_change())
    

@router_admin.callback_query(F.data.lower() == "cancel")
async def add(callback: CallbackQuery):
    await callback.message.answer(text="Выберите действие",\
                                reply_markup=menu_main)
    

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
    
@router_admin.callback_query(F.data.lower() == "change_photo")
async def change(callback: CallbackQuery):
    await callback.message.edit_text(text="Photo change", reply_markup=admin_panel())


@router_admin.callback_query(F.data.lower() == "change_change")
async def change(callback: CallbackQuery):
    await callback.message.edit_text(text="description change", reply_markup=admin_panel())
    

@router_admin.callback_query(F.data.lower() == "change_price")
async def change(callback: CallbackQuery):
    await callback.message.edit_text(text="price change", reply_markup=admin_panel())


@router_admin.callback_query(F.data.lower() == "change_cancel")
async def change(callback: CallbackQuery):
    await callback.message.edit_text(text=(f"Вы {callback.from_user.full_name} в админ панели"),\
                                reply_markup=admin_panel())