from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def arrange_inline_schema(buttons: List[InlineKeyboardButton], count: List[int]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.row_width = max(count)
    if sum(count) != len(buttons):
        raise ValueError('Количество кнопок не совпадает со схемой')
    tmplist = []
    for a in count:
        tmplist.append([])
        for _ in range(a):
            tmplist[-1].append(buttons.pop(0))
    kb.inline_keyboard = tmplist
    return kb
