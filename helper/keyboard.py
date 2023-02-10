from pykeyboard import InlineKeyboard
from pyrogram.types import InlineKeyboardButton
from utils.functions import get_urls_from_text

def keyboard(buttons_list, row_width: int = 2):
    buttons = InlineKeyboard(row_width=row_width)
    data = [
        (
            InlineKeyboardButton(text=str(i[0]), callback_data=str(i[1]))         
            if not get_urls_from_text(i[1])
            else InlineKeyboardButton(text=str(i[0]), url=str(i[1]))
        )
        for i in buttons_list
    ]
    buttons.add(*data)
    return buttons


def ikb(data: dict, row_width: int = 2):
    return keyboard(data.items(), row_width=row_width)
