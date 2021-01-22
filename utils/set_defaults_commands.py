from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("auth", "Отправить данные для авторизации"),
        types.BotCommand("token", "Получить токен"),
        types.BotCommand("save", "Сохранить токен в базу данных"),
        types.BotCommand("posts", "Получить посты"),
        types.BotCommand("help", "Помощь")
    ])
