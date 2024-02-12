from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery, InlineKeyboardButton
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder

from configs import msg

router_mini_wallet = Router()

###############  Keybord #################
def inline_product():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🔎ОПИСАНИЕ", callback_data="description")
    ), builder.adjust(1)
    return builder.as_markup(resize_keyboard=True,
                             input_field_placeholder=msg.TEXT_CHOICE_1)

def inline_product_order():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🛒ЗАКАЗАТЬ", callback_data="description_order")
    ), builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


################## output ###################

@router_mini_wallet.callback_query(F.data == "description")
async def output_product(callback: CallbackQuery):
    album = MediaGroupBuilder()
    photos = ["configs/media/product_description/1.png",
            "configs/media/product_description/2.png",
            "configs/media/product_description/3.png",
            "configs/media/product_description/4.png"]
    for photo in photos:
        album.add(type="photo", media=FSInputFile(photo))
    await callback.message.answer(text="<b>👇Мини кошелёк👇</b>")
    await callback.message.answer_media_group(media=album.build())
    await callback.message.answer(text=MINI_WALLET, reply_markup=inline_product_order())


@router_mini_wallet.callback_query(F.data == "description_order")
async def description_order(callback: CallbackQuery):
    await callback.message.answer(text=" Вы закали ") # здесь работа с базой данных


################### Описание изделия ##################

MINI_WALLET = (f"🧳<b>Мини кошелёк</b>\n"
               f"🔎Описание:\n"
               f"Кошелек подходит мужчинвм и женщинам❕\n"
               f"Ручная работа❕\n"
               f"Натуральная кожа умершего животного❕\n"
               f"✂Обработка изделия:\n"
               f" -воск пчелиный;\n"
               f" -аппретура (крем) Kenda Farben (Италия);\n"
               f" -средство для уреза FIEBING'S (Америка).\n"
               f"🪡Прошито изделие седельным швом\n"
               f"вощённо-плетёнными нитями 0.7 мм.\n"
               f"🔎Характеристики:\n"
               f" -4 отделения под карты;\n"
               f" -одно отделение под купюры\n"
               f"(в сложенном виде).\n"
               f"⁉Прослужит данное изделия года, и с\n"
               f"каждым годом кожа будет становиться\n"
               f"благороднее.")