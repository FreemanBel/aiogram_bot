import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.storage import FSMContext

from loader import dp
from states import UserData


@dp.message_handler(Command('auth'))
async def get_user_data(message: types.Message):
    await message.answer("Введите <b>username</b> и\nотправьте его боту!")
    await UserData.first()


@dp.message_handler(state=UserData.username)
async def get_email(message: types.Message, state: FSMContext):
    username = message.text
    await state.update_data(
            {
                "username": username
            }
    )
    await message.reply("Сообщение удалится через 2 секунды.")
    await asyncio.sleep(2)
    await message.delete()
    await message.answer("<b>username</b> зафиксирован в машине сосотояний.")

    await message.answer("Введите <b>password</b>\n"
                         "и отправьте его боту!")
    await UserData.next()


@dp.message_handler(state=UserData.password)
async def get_email(message: types.Message, state: FSMContext):
    password = message.text
    await state.update_data(
            {
                "password": password
            }
    )
    await message.reply("Сообщение будет удалено через 2 секунды.")
    await asyncio.sleep(2)
    await message.delete()
    await message.answer("<b>password</b> зафиксирован в машине сосотояний.")

    data = await state.get_data()
    username = data.get('username')
    password = data.get('password')
    await message.answer(
            "Данные были внесены в машину состояний\n"
            "и могут быть использованы для получения токена."
    )

    await state.reset_state(with_data=False)
