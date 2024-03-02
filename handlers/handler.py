import os
from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command
from aiogram.utils.media_group import MediaGroupBuilder

from handlers import keyboard, women_wallet_kenya, product
from configs import msg
from admin.admin_inline_kb import admin_panel
from database.admin_db import AdminDB

admin_db = AdminDB()
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=(f"Привет <b>{message.from_user.full_name}</b>.\n"
                            f"{msg.CMD_START}"), reply_markup=keyboard.menu_main)


@router.message(Command("admin"))
async def admin(message: Message):
    if message.from_user.id == int(os.getenv("ADMIN_ID")):
        await message.answer(text=f"Привет {message.from_user.full_name}",\
                             reply_markup=keyboard.menu_main)
        await message.answer(text=("Добро пожаловать в админ панель"),\
                             reply_markup=admin_panel())
    else: 
        await message.answer("Нет такой команды!")
    

@router.message(F.text.upper() == "🔎 О НАС")
async def production_process(message: Message):
    await message.answer(text=(f"Привет <b>{message.from_user.full_name}</b>, "
                               f"меня зовут <b>Эдуард</b>.\n"
                               f"{msg.ABOUT_US}"),
                         reply_markup=keyboard.production_process)
    await message.delete()


@router.message(F.text.upper() == "👀 ИЗДЕЛИЯ")
async def products(message: Message):
    showcase = admin_db.showcase_photo_db()
    for i in showcase:
        await message.answer_photo(photo=i,\
                                reply_markup=product.inline_product())


@router.message(F.text.upper() == "🛠 ИСПОЛЬЗУЕМЫЕ ИНСТРУМЕНТЫ")
async def tools_used(message: Message):
    album = MediaGroupBuilder()
    photos = {"configs/media/insrument_chemistry/tools.png": msg.TOOLS,\
              "configs/media/insrument_chemistry/tools 1.png": msg.TOOLS_1,\
              "configs/media/insrument_chemistry/tools 2.png": msg.TOOLS_2,\
              "configs/media/insrument_chemistry/tools 3.png": msg.TOOLS_3,\
              "configs/media/insrument_chemistry/tools 4.png": msg.TOOLS_4,\
              "configs/media/insrument_chemistry/tools 5.png": msg.TOOLS_5}    
    for k, v in photos.items():
        album.add(type="photo", media=FSInputFile(k), 
                caption=v)
    await message.answer_media_group(media=album.build())


@router.message(F.text.upper() == "✂ ОБРАБОТКА КОЖИ")
async def chemistry(message: Message):
    await message.answer_photo(photo=FSInputFile("configs/media/insrument_chemistry/chemistry.png"),\
                               caption=msg.CHEMISTRY)
    

@router.message(F.text.upper() == "🚚 УСЛОВИЯ ДОСТАВКИ")
async def delivery_terms(message: Message):
    await message.answer(text=msg.DELIVERY_TERMS)
    

@router.message(F.text.upper() == "НАЗАД")
async def trash_text(message: Message):
    await message.answer(text=(f"{message.from_user.full_name}.\n"
                               f"{msg.TEXT_CHOICE_1}"), reply_markup=keyboard.menu_main)
    await message.delete()
    

# @router.message()
# async def trash_text(message: Message):
#     await message.answer(text=(f"{message.from_user.full_name}.\n"
#                                f"{msg.TEXT_CHOICE_1}"), reply_markup=keyboard.menu_main)