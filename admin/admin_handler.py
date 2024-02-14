from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.utils.media_group import MediaGroupBuilder

from admin.admin_inline_kb import admin_panel_add, admin_panel_change, admin_panel
from handlers.keyboard import menu_main


router_admin = Router()

################## admin_panel #######################

@router_admin.callback_query(F.data.lower() == "add")
async def add(callback: CallbackQuery):
    await callback.message.edit_text(text="Выберите действие",\
                                reply_markup=admin_panel_add())


@router_admin.callback_query(F.data.lower() == "change")
async def add(callback: CallbackQuery):
    await callback.message.edit_text(text="Выберите действие",\
                                  reply_markup=admin_panel_change())
    

@router_admin.callback_query(F.data.lower() == "cancel")
async def add(callback: CallbackQuery):
    await callback.message.answer(text="Выберите действие",\
                                reply_markup=menu_main)
    

################## button add #######################

@router_admin.callback_query(F.data.lower() == "add_photo")
async def add(callback: CallbackQuery):
    await callback.message.edit_text(text="Photo", reply_markup=admin_panel())


@router_admin.callback_query(F.data.lower() == "add_change")
async def add(callback: CallbackQuery):
    await callback.message.edit_text(text="description", reply_markup=admin_panel())
    

@router_admin.callback_query(F.data.lower() == "add_price")
async def add(callback: CallbackQuery):
    await callback.message.edit_text(text="price", reply_markup=admin_panel())
    

@router_admin.callback_query(F.data.lower() == "add_cancel")
async def add(callback: CallbackQuery):
    await callback.message.edit_text(text=(f"Вы {callback.from_user.full_name} в админ панели"),\
                                reply_markup=admin_panel())
    


#################### button change #####################
    
@router_admin.callback_query(F.data.lower() == "change_photo")
async def add(callback: CallbackQuery):
    await callback.message.edit_text(text="Photo change", reply_markup=admin_panel())


@router_admin.callback_query(F.data.lower() == "change_change")
async def add(callback: CallbackQuery):
    await callback.message.edit_text(text="description change", reply_markup=admin_panel())
    

@router_admin.callback_query(F.data.lower() == "change_price")
async def add(callback: CallbackQuery):
    await callback.message.edit_text(text="price change", reply_markup=admin_panel())


@router_admin.callback_query(F.data.lower() == "change_cancel")
async def add(callback: CallbackQuery):
    await callback.message.edit_text(text=(f"Вы {callback.from_user.full_name} в админ панели"),\
                                reply_markup=admin_panel())