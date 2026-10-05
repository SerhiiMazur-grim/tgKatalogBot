from typing import List

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup


def galery_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardBuilder()
    
    ikb.button(text='Барні меблі', callback_data='bar')
    ikb.button(text='Буфети', callback_data='byfet')
    ikb.button(text='Дивани', callback_data='duvan')
    ikb.button(text='Комоди', callback_data='komod')
    ikb.button(text='Крісла', callback_data='krislo')
    ikb.button(text='Ліжка', callback_data='lijko')
    ikb.button(text='Обідні стільці', callback_data='obid_stilci')
    ikb.button(text='Обідні столи', callback_data='obid_stolu')
    ikb.button(text='Передпокій', callback_data='peredpokiy')
    ikb.button(text='Письмові столи', callback_data='pusmovi_stolu')
    ikb.button(text='Приліжкові', callback_data='prulijku')
    ikb.button(text='Серванти', callback_data='servantu')
    ikb.button(text='Софи', callback_data='sofu')
    ikb.button(text='Стелажі', callback_data='stelaji')
    ikb.button(text='Столики', callback_data='stoluku')
    ikb.button(text='Тумби під TV', callback_data='tv')
    
    ikb.adjust(3)
    
    return ikb.as_markup()