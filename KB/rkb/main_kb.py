from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup


def main_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='Каталог')
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
