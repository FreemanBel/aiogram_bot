import emoji
import requests
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hunderline

from loader import dp, db, bot


@dp.message_handler(Command('posts'))
async def get_posts(message: types.Message):
    get = db.connect()
    user_id = message.from_user.id
    query = 'SELECT token FROM USERS WHERE user_id=?'
    get_token = get.execute(query, (user_id,))
    token = get_token.fetchone()[0]

    # url = 'https://experts-community.herokuapp.com/api'
    url = 'http://127.0.0.1:8000/api'
    headers = {'Authorization': f'Token {token}'}
    resp = requests.get(url, headers=headers)
    posts = resp.json()

    count = posts['count']
    await message.answer(f'Всего на сайте опубликовано {count} постов.')

    for i in range(len(posts['results'])):
        await message.answer(
                (emoji.emojize(":rocket:") * 10) + '\n' +
                'Автор: ' + hunderline(str(posts['results'][i]['author']['first_name']) + ' '
                + str(posts['results'][i]['author']['last_name'])) + '\n'
                + 'Название: ' + str(posts['results'][i]['title']) + '\n'
                + 'Дата: ' + str(posts['results'][i]['created_at'][:10]) + '\n'
                + (emoji.emojize(":rocket:") * 10)
        )
