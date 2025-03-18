import os
import sys
import asyncio

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv, find_dotenv
from .handlers import start_router
from apps.exchanges import exchange_router
from bot.commands import commands

load_dotenv(find_dotenv())


bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(exchange_router)


# ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=commands,
                              scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
