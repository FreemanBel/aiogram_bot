import emoji
import requests
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hunderline, hitalic, code, bold
from environs import Env

from loader import dp, db

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

@dp.message_handler(Command('posts'))
async def get_posts(message: types.Message):
    get = db.connect()
    user_id = message.from_user.id
    query = 'SELECT token FROM USERS WHERE user_id=?'
    get_token = get.execute(query, (user_id,))
    token = get_token.fetchone()[0]

    url = 'https://experts-community.herokuapp.com/api'

    headers = {'Authorization': f'Token {token}'}
    resp = requests.get(url, headers=headers)
    posts = resp.json()

    count = posts['count']
    await message.answer(f'Всего на сайте опубликовано {count} постов.')
    book = []

    for i in range(len(posts['results'][:2])):
        await message.answer(
                (emoji.emojize(":rocket:") * 10) + '\n' +
                ('Автор:) ' + hunderline(str(posts['results'][i]['author']['first_name']) + ' '
                                         + str(posts['results'][i]['author']['last_name']))) + '\n'
                + 'Название: ' + str(posts['results'][i]['title']) + '\n'
                + 'Содержание: ' + hitalic(str(posts['results'][i]['content'])) + '\n'
                + 'Дата: ' + code(str(posts['results'][i]['created_at'][:10])) + '\n'
                + (emoji.emojize(":rocket:") * 10)
        )


class AllPosts():
    def __init__(self, book=[]):
        self._book = book

    def get_all_posts(self):
        get = db.connect()
        user_id = env.int("ADMINS")
        query = 'SELECT token FROM USERS WHERE user_id=?'
        get_token = get.execute(query, (user_id,))
        token = get_token.fetchone()[0]

        url = 'https://experts-community.herokuapp.com/api'
        headers = {'Authorization': f'Token {token}'}
        resp = requests.get(url, headers=headers)
        posts = resp.json()

        count = posts['count']
        book = self._book
        _ = '\n__________________________________\n'
        for i in range(len(posts['results'])):
            book.append((emoji.emojize(":rocket:") * 3 + hitalic(f'Всего {count} страниц.' + emoji.emojize(
                    ":rocket:") * 3 +
                               f'{_}')) + '\n' +
                        ('Автор: ' + hunderline(str(posts['results'][i]['author']['first_name']) + ' '
                                                 + str(posts['results'][i]['author']['last_name'])))
                        + f'{_}'
                        + 'Название: ' + str(posts['results'][i]['title'])
                        + f'{_}'
                        + 'Содержание: \n' + hitalic(str(posts['results'][i]['content']))
                        + f'{_}'
                        + 'Дата: ' + code(str(posts['results'][i]['created_at'][:10])), )
        return book
