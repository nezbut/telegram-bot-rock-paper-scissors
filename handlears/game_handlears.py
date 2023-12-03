from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from utils.game_utils import user_winner
from utils.users_status import UsersInGame
from keyboards.bot_keyboards import get_keyboard_yes_and_no, get_keyboard_game
from random import choice

router = Router()

@router.message(F.text == LEXICON_RU['yes_button'])
async def user_yes_button_handlear(message: Message):
    if message.from_user.id not in UsersInGame.USERS:
        UsersInGame.add_user(message.from_user.id)
        await message.answer(
            text=LEXICON_RU['yes'],
            reply_markup=get_keyboard_game()
        )

@router.message(F.text == LEXICON_RU['no_button'])
async def user_no_button_handlear(message: Message):
    if message.from_user.id not in UsersInGame.USERS:
        await message.answer(
            text=LEXICON_RU['no'](LEXICON_RU['yes_button'])
        )

@router.message(F.text.in_(LEXICON_RU['game_elements']))
async def user_answer_game_elements(message: Message):
    if message.from_user.id in UsersInGame.USERS:
        bot_answer = choice(LEXICON_RU['game_elements'])
        user_win = user_winner(bot_answer=bot_answer, user_answer=message.text)

        await message.answer(f"{LEXICON_RU['bot_answer']}: {bot_answer}")

        if user_win:
            await message.answer(
                LEXICON_RU['user_won'],
                reply_markup=get_keyboard_yes_and_no()
            )

        elif user_win is None:
            await message.answer(
                LEXICON_RU['nobody_won'],
                reply_markup=get_keyboard_yes_and_no()
            )

        else:
            await message.answer(
                LEXICON_RU['bot_won'],
                reply_markup=get_keyboard_yes_and_no()
            )

        UsersInGame.delete_user(message.from_user.id)
