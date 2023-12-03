from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_RU

def get_keyboard_yes_and_no() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text=LEXICON_RU['yes_button']), KeyboardButton(text=LEXICON_RU['no_button'])]
    ]
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=True
    )

def get_keyboard_game() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    buttons = [KeyboardButton(text=text_btn) for text_btn in LEXICON_RU['game_elements']]
    builder.add(*buttons)
    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

__all__ = (
    'get_keyboard_yes_and_no',
    'get_keyboard_game'
)
