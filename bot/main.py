import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

from handlers.start import start_router

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()
dp.include_router(start_router)

# ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
