from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.bot_keyboards import get_keyboard_yes_and_no

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['start'],
        reply_markup=get_keyboard_yes_and_no()
    )


@router.message(Command(commands=["help"]))
async def help_command(message: Message):
    await message.answer(text=LEXICON_RU['help'](message.from_user.full_name))
