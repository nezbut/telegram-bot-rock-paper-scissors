from aiogram import Dispatcher, Bot
from handlears import commands_handlears, game_handlears
from config.config_data import Config

import asyncio
import logging

async def main():
    bot = Bot(token=Config.tg_bot.bot_token)
    dp = Dispatcher()

    dp.include_routers(
        commands_handlears.router,
        game_handlears.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
