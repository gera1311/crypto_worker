from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_keyboard = ReplyKeyboardBuilder()
start_keyboard.add(
    KeyboardButton(text='Главное меню'),
    KeyboardButton(text='О боте'),
    KeyboardButton(text='Связь с разработчиком')
)
start_keyboard.adjust(2, 1)
start_keyboard = start_keyboard.as_markup(resize_keyboard=True)

menu_keyboard = ReplyKeyboardBuilder()
menu_keyboard.add(
    KeyboardButton(text='Массовый вывод с биржи'),
    KeyboardButton(text='Чекер балансов'),
    KeyboardButton(text='Управление кошельками'),
    KeyboardButton(text='Получить курс криптовалюты'),
)

menu_keyboard.adjust(2, 2)
menu_keyboard = menu_keyboard.as_markup(resize_keyboard=True)
