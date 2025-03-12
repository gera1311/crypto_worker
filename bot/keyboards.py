from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


start_keyboard = ReplyKeyboardBuilder()
start_keyboard.add(
    KeyboardButton(text='Главное меню'),
    KeyboardButton(text='О боте'),
    KeyboardButton(text='Связь с разработчиком')
)
start_keyboard.adjust(2, 1)
start_keyboard = start_keyboard.as_markup(
    resize_keyboard=True,
    placeholder='Выбери действие'
)


menu_keyboard = InlineKeyboardBuilder()
menu_keyboard.add(
    InlineKeyboardButton(text='Мои биржи',
                         callback_data='my_exchanges'),
    InlineKeyboardButton(text='Привязать биржу',
                         callback_data='attach_exchange'),
    InlineKeyboardButton(text='Отвязать биржу',
                         callback_data='detach_exchange'),
    InlineKeyboardButton(text='Массовый вывод средств',
                         callback_data='mass_withdrawal'),
    InlineKeyboardButton(text='Назад',
                         callback_data='back_to_main_menu')
)
menu_keyboard.adjust(2, 2, 1)
menu_keyboard = menu_keyboard.as_markup()
