from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from .get_posts import get_posts
from data.content import max_pages_book, book
from keyboards.inline.pagination import get_page_keyboard, pagination_call
from loader import dp
from utils.misc.pages import get_page




@dp.message_handler(Command("book"))
async def show_book(message: types.Message):
    text = get_page(book)
    await message.answer(text,
                         reply_markup=get_page_keyboard(max_pages=max_pages_book))


@dp.callback_query_handler(pagination_call.filter(page="current_page"))
async def current_page_error(call: CallbackQuery):
    await call.answer(cache_time=60)


@dp.callback_query_handler(pagination_call.filter(key="book"))
async def show_chosen_page(call: CallbackQuery, callback_data: dict):
    current_page = int(callback_data.get("page"))
    text = get_page(book, page=current_page)
    markup = get_page_keyboard(max_pages=max_pages_book, page=current_page)
    await call.message.edit_text(text=text, reply_markup=markup)

