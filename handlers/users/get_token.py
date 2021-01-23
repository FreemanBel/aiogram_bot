import emoji
import requests
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.storage import FSMContext

from loader import dp, db


@dp.message_handler(Command('token'))
async def get_auth_token(message: types.Message, state: FSMContext):
    await message.answer(emoji.emojize(":rocket:") * 10)
    data = await state.get_data()
    username = data.get('username')
    password = data.get('password')
    auth = requests.post(f'https://experts-community.herokuapp.com/api/api-token-auth/',
                         {
                             'username': f'{username}',
                             'password': f'{password}'
                         }
                         )
    response = auth.json()
    token = response['token']

    insert = db
    user_id = message.from_user.id
    insert.insert_token(
            conn=insert.connect(),
            token=token,
            user_id=user_id
    )
    await message.answer('Token получен и сохранен в базе данных.')
