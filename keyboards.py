from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='/token'),
            KeyboardButton(text='/login'),

        ],
        [
            KeyboardButton(text="https://experts-community.herokuapp.com/posts/posts/"),
        ],
    ],
    resize_keyboard=True
)