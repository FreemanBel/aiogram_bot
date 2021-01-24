from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("auth", "Отправить данные для авторизации"),
        types.BotCommand("token", "Получить токен"),
        types.BotCommand("subscribe","Подписаться на канал уведомлений"),
        types.BotCommand("posts", "Получить два последних поста"),
        types.BotCommand("book", "Получить все посты в виде книги"),
        types.BotCommand("help", "Помощь")
    ])