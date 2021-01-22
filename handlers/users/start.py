from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
import json


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Приветствую, <b>{message.from_user.full_name}<b/> "
                         f"(ID: <code>{message.from_user.id}</code>)!\n"
                         f"Для того чтоб познакомиться с возможностями бота\n"
                         f"введите /help для просмотра всех комманд."
                         )
