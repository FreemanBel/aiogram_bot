import logging
import requests
from config import BOT_TOKEN
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards import menu
from aiogram.dispatcher.filters import Command, Text
from aiogram import Bot, Dispatcher, executor, types


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply(
        "Бот запущен! \n"
        "**********************************************************************************************\n"
        "1) Чтобы получить Token для авторизации введите логин и пароль через пробел и отправьте боту,"
        " затем нажмите /token \n"
        "**********************************************************************************************\n"
        "2) Отправьте боту Token и нажмите /login"
        "**********************************************************************************************\n",
        reply_markup=menu
    )


@dp.message_handler(commands=['token'])
async def get_token(message: Message):
    auth = requests.post(f'http://127.0.0.1:8000/api/api-token-auth/',
                         {'username': f'{login_data.split()[0]}', 'password': f'{login_data.split()[1]}'})
    response = auth.json()
    await message.reply(response)


@dp.message_handler(commands=['login'])
async def login(message: types.Message):
    url = 'http://127.0.0.1:8000/api/'
    headers = {'Authorization': f'Token {login_data}'}
    resp = requests.get(url, headers=headers)
    response = resp.json()
    await message.reply(response)


@dp.message_handler()
async def get_TOKEN(message: types.Message):
    global login_data
    login_data = message.text


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
