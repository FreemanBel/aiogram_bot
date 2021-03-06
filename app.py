from aiogram import executor

from loader import dp, db, scheduler
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_defaults_commands import set_default_commands
# from handlers.users.read_posts import show_book
#
#
#
# def sheduler_jobs():
#     scheduler.add_job(show_book, "interval", seconds=5)



async def on_startup(dispatcher):
    # Уведомляет про запуск
    await on_startup_notify(dp)
    await set_default_commands(dp)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
    sheduler_jobs()
