from typing import Any, Final, TYPE_CHECKING

import asyncio
import logging
import sys

from aiogram import Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from KB import rkb

router: Final[Router] = Router(name=__name__)


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text = f"Hello, {html.bold(message.from_user.full_name)}!",
                         reply_markup = rkb.main_keyboard())
