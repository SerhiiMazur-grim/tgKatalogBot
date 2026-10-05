import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from handlers import comands, katalog

TOKEN = '8804496300:AAGYIAaiIxExEnNaxnYo9TEjWHQIWcGyNvA'

dp = Dispatcher()
dp.include_routers(
    comands.router,
    katalog.router
)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())