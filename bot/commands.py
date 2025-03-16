from aiogram.types import BotCommand


commands = [
    BotCommand(command='start', description='Запуск бота'),
    BotCommand(command='menu', description='Посмотреть меню'),
    BotCommand(command='exchange', description='Работа с биржами'),
    BotCommand(command='wallet', description='Работа с кошельками'),
    BotCommand(command='about', description='О боте'),
]
