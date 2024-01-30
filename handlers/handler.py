from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from handlers import keyboard


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text="Описание", reply_markup=keyboard.menu_main)