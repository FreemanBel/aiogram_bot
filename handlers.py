import logging
import requests
import asyncio
from config import BOT_TOKEN, admin_id
from aiogram.types import Message
from keyboards import menu
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
loop = asyncio.get_event_loop()
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)


@dp.message_handler(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer(
                        text='<b>Бот запущен!</b>\n'
                              'Отправьте боту логин и пароль\n'
                              'через пробел,\n'
                              'затем нажмите\n'
                              '/save',
                        reply_markup=menu
                         )


@dp.message_handler(commands=['save'])
async def save_into_data(message: Message):
    from db import DbConnect
    insert = DbConnect()
    insert.create_db(conn=insert.connect())
    user_id = message.from_user.id
    insert.insert(
        conn=insert.connect(),
        user_id=user_id,
        username=login_data.split()[0],
        password=login_data.split()[1]
    )
    await message.answer(text='<b>Данные сохранены в базу!</b>\n'
                              'Теперь нажмите /posts\n'
                              'для получения постов\n'
                              'в формате JSON'
                         )


@dp.message_handler(commands=['posts'])
async def get_posts(message: Message):
    from db import DbConnect
    get_ = DbConnect().connect()
    user_id = message.from_user.id
    query = "SELECT username, password FROM USERS WHERE user_id=?"
    res = get_.execute(query, (user_id,))
    row = res.fetchone()
    auth = requests.post(f'https://experts-community.herokuapp.com/api/api-token-auth/',
                         {'username': f'{row[0]}', 'password': f'{row[1]}'})
    response = auth.json()
    token = response['token']
    url = 'https://experts-community.herokuapp.com/api'
    headers = {'Authorization': f'Token {token}'}
    resp = requests.get(url, headers=headers)
    posts = resp.json()
    await message.reply(posts)



@dp.message_handler()
async def into_insert(message: types.Message):
    global login_data
    login_data = message.text


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
