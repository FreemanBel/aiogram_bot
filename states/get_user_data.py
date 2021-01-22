from aiogram.dispatcher.filters.state import StatesGroup, State


class UserData(StatesGroup):
    username = State()
    password = State()