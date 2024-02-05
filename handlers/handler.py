from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart

from handlers import keyboard
from configs import msg


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):   
    await message.answer(text=(f"Привет <b>{message.from_user.full_name}</b>.\n"
                               f"{msg.CMD_START}"), reply_markup=keyboard.menu_main)
    

@router.message(F.text.upper() == "🔎 О НАС")
async def production_process(message: Message):
    await message.answer(text=(f"Привет <b>{message.from_user.full_name}</b>, "
                               f"меня зовут <b>Эдуард</b>.\n"
                               f"{msg.ABOUT_US}"),
                         reply_markup=keyboard.production_process)
    await message.delete()


@router.message(F.text.upper() == "🛠 ИСПОЛЬЗУЕМЫЕ ИНСТРУМЕНТЫ")
async def tools_used(message: Message):
    photos = {"configs/photo/tools.png": msg.TOOLS,\
              "configs/photo/tools 1.png": msg.TOOLS_1,\
              "configs/photo/tools 2.png": msg.TOOLS_2,\
              "configs/photo/tools 3.png": msg.TOOLS_3,\
              "configs/photo/tools 4.png": msg.TOOLS_4,\
              "configs/photo/tools 5.png": msg.TOOLS_5}    
    for k, v in photos.items():
        await message.answer_photo(photo=FSInputFile(k), caption=v)


@router.message(F.text.upper() == "✂ ОБРАБОТКА КОЖИ")
async def chemistry(message: Message):
    await message.answer_photo(photo=FSInputFile("configs/photo/chemistry.png"),\
                               caption=msg.CHEMISTRY)


@router.message(F.text.upper() == "НАЗАД")
async def trash_text(message: Message):
    await message.answer(text=(f"{message.from_user.full_name}.\n"
                               f"{msg.TEXT}"), reply_markup=keyboard.menu_main)
    await message.delete()
    

# @router.message()
# async def trash_text(message: Message):
#     await message.answer(text=(f"{message.from_user.full_name}.\n"
#                                f"{msg.TEXT}"), reply_markup=keyboard.menu_main)