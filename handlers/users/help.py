from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/auth - Отправить данные для авторизации",
            "/token - Получить токен авторизации",
            "/posts - Получить два последних поста",
            "/book - Получить все посты в виде книги",
            "/subscribe - Подписаться на канал уведомлений",
            "/help - Получить справку"
            )
    
    await message.answer("\n".join(text))
