import asyncio
import logging
import time

from aiogram import Bot, Dispatcher

from configs.config import conf_settigs
from handlers.handler import router
from handlers.mini_wallet import router_mini_wallet
from handlers.women_wallet_kenya import router_women_wallet_kenya
from admin.admin_handler import router_admin


async def main():
    dp.include_routers(router, router_mini_wallet,\
                        router_women_wallet_kenya, router_admin)
    # удаляет команды (когда откл.бот)  
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def times():
    time_time = time.time()
    local_time = time.localtime(time_time)
    format_time = time.strftime("%m-%d | %H:%M", local_time)
    return format_time


if __name__ == "__main__":
    bot = Bot(token=conf_settigs.token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)
    try:
        print(f"\nБот начал работу!\n   {times()}\n")
        asyncio.run(main())
        asyncio.run()
    except KeyboardInterrupt:
        print(f"\nБот завершил работу!\n   {times()}\n")