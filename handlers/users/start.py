from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    insert = db
    insert.create_db(conn=insert.connect())
    user_id = message.from_user.id
    insert.insert_user_id(
            conn=insert.connect(),
            user_id=user_id,
    )
    await message.answer(f"Приветствую, <b>{message.from_user.full_name}!</b>\n"
                         f"<b><i>Bot</i></b> запомнил Ваш ID: <code>{message.from_user.id}</code>,\n"
                         f"Вы теперь в базе данных!\n\n\n"
                         f"Для того чтоб познакомиться с возможностями бота\n"
                         f"введите /help для просмотра всех комманд."
                         )
