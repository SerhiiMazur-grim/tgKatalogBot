from __future__ import annotations

from typing import Any, Final

from aiogram import Router, F
from aiogram.methods import TelegramMethod
from aiogram.types import Message, CallbackQuery, InputMediaPhoto

from KB import ikb
from katalog import IDS


router: Final[Router] = Router(name=__name__)


@router.message(F.text == 'Каталог')
async def katalog_handler(message: Message) -> TelegramMethod:
    await message.delete()
    return message.answer(text='Оберіть категорію⤵️',
                          reply_markup=ikb.galery_ikb())


@router.message(lambda message: message.photo)
async def photo_handler(message: Message) -> TelegramMethod:
    id = message.photo[-1].file_id
    print(id)


@router.callback_query()
async def get_catalog(call: CallbackQuery) -> TelegramMethod:
    await call.message.delete()
    data = call.data
    ids = IDS.get(data)
    if ids:
        for i in range(0, len(ids), 10):
            chunk = ids[i:i + 10]

            media = [
                InputMediaPhoto(media=file_id)
                for file_id in chunk
            ]

            await call.message.answer_media_group(
                media=media
            )
        await call.message.answer(text='🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦')
    else:
        await call.message.answer(text='Каталог пустий, зверніться до адміністратора')
