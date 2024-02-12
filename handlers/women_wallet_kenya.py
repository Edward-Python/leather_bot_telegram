from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery, InlineKeyboardButton
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder

from configs import msg

router_women_wallet_kenya = Router()

###############  Keybord #################
def inline_product():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🔎ОПИСАНИЕ", callback_data="description_1")
    ), builder.adjust(1)
    return builder.as_markup(resize_keyboard=True,
                             input_field_placeholder=msg.TEXT_CHOICE_1)

def inline_product_order():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="🛒ЗАКАЗАТЬ", callback_data="description_order_1")
    ), builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


################## output ###################

@router_women_wallet_kenya.callback_query(F.data == "description_1")
async def output_product(callback: CallbackQuery):
    album = MediaGroupBuilder()
    photos = ["configs/media/women_wallet_kenya/1.png",
              "configs/media/women_wallet_kenya/2.png",
              "configs/media/women_wallet_kenya/3.png",
              "configs/media/women_wallet_kenya/4.png",
              "configs/media/women_wallet_kenya/5.png"]
    for photo in photos:
        album.add(type="photo", media=FSInputFile(photo))
    await callback.message.answer(text="<b>👇Женский кошелёк \"Кения\"👇</b>")
    await callback.message.answer_media_group(media=album.build())
    await callback.message.answer(text=women_wallet_kenya, reply_markup=inline_product_order())


@router_women_wallet_kenya.callback_query(F.data == "description_order_1")
async def description_order(callback: CallbackQuery):
    await callback.message.answer(text=" Jnrfp? ytn d yfkbxb ") # здесь работа с базой данных


################### Описание изделия ##################
    
women_wallet_kenya = (f"🧳<b>Женский кошелёк \"Кения\".</b>\n"
                      f"🔎Описание:\n"
                      f"Ручная работа❕\n"
                      f"Натуральная кожа умершего животного❕\n"
                      f"✂Обработка изделия:\n"
                      f" -воск пчелиный;\n"
                      f" -аппретура (крем) Kenda Farben (Италия);\n"
                      f" -средство для уреза FIEBING'S (Америка).\n"
                      f"🪡Прошито изделие седельным швом\n"
                      f"вощённо-плетёнными нитями 0.7 мм.\n"
                      f"🔎Характеристики:\n"
                      f" -6 отделения под карты;\n"
                      f" -одно отделение под купюры\n"
                      f"(в развёрнутом виде).\n"
                      f"⁉Прослужит данное изделия года, и с\n"
                      f"каждым годом кожа будет становиться\n"
                      f"благороднее.")