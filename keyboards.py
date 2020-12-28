from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/save'),
            KeyboardButton(text='/posts'),
        ],

    ],
    resize_keyboard=True
)
