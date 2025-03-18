from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart, or_f

from .keyboards import get_inline_keyboard

start_router = Router()

TEXT_START = ("Привет, {name}! Я твой персональный помощник.")

START_KEYBOARD = get_inline_keyboard(
    ('Главное меню', 'menu'),
    ('О боте', 'about_bot'),
    placeholder='Что вы хотели?',
    sizes=(1, 1)
)

MENU_KEYBOARD = get_inline_keyboard(
    ('Аккаунт', 'accounts'),
    ('Биржи', 'exchanges'),
    ('Кошельки', 'wallets'),
    ('Помощь', 'help'),
    ('Назад', 'back'),
    ('Отмена', 'cancel'),
    placeholder='Что вы хотели?',
    sizes=(1, 2, 1, 2)
)

ACCOUNT_KEYBOARD = get_inline_keyboard(
    ('Мои биржи', 'accounts'),
    ('Мои кошельки', 'accounts'),
    ('Назад', 'back'),
    ('Отмена', 'cancel'),
    placeholder='Информация об аккаунте',
    sizes=(2, 2)
)

WALLET_KEYBOARD = get_inline_keyboard(
    ('Мои биржи', 'accounts'),
    ('Мои кошельки', 'accounts'),
    ('Назад', 'back'),
    ('Отмена', 'cancel'),
    placeholder='Информация об аккаунте',
    sizes=(2, 2)
)


@start_router.message(CommandStart())
async def start_menu(message: types.Message):
    await message.answer(
        f'{TEXT_START.format(name=message.from_user.first_name)} '
        f'Выбери действие из главного меню:', reply_markup=START_KEYBOARD
    )
    await message.delete()


@start_router.callback_query(or_f(F.data == 'start', F.data == 'back_start'))
async def start_menu_callback(callback: types.CallbackQuery):
    await callback.message.answer(
        'Выберите действие из главного меню:', reply_markup=START_KEYBOARD
    )
    await callback.message.delete()
    await callback.answer()


@start_router.message(
        or_f(Command('menu'), F.text.lower().contains('меню')))
async def main_menu(message: types.Message):
    await message.answer(
        'С чем вы хотите работать?', reply_markup=MENU_KEYBOARD
    )
    await message.delete()


@start_router.callback_query(F.data == 'menu')
async def main_menu_callback(callback: types.CallbackQuery):
    await callback.message.answer(
        'С чем вы хотите работать?', reply_markup=MENU_KEYBOARD
    )
    await callback.message.delete()
    await callback.answer()
