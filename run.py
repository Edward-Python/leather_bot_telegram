import asyncio
import logging
import time

from aiogram import Bot, Dispatcher

from configs.config import conf_settigs
from handlers.product import product_router
from handlers.handler import router
from fsm_mashine.admin_handler import router_admin
from fsm_mashine.user_handler import router_user


async def main():
    dp.include_routers(router,\
                       router_user,\
                        router_admin,\
                        product_router)
    # удаляет запросы (когда откл.бот) 
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