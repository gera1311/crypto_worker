from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart, or_f

from keyboards import get_inline_keyboard

start_router = Router()

TEXT_START = ("привет! Я твой персональный помощник.")


async def send_start_keyboard(message: types.Message,
                              delete_original: bool = False):
    await message.answer(
        text="Выберите действие из главного меню:",
        reply_markup=get_inline_keyboard(
            ('Главное меню', 'menu'),
            ('О боте', 'about_bot'),
            placeholder='Что вы хотели?',
            sizes=(1, 1)
        )
    )
    if delete_original:
        await message.delete()


async def send_menu_keyboard(message: types.Message,
                             delete_original: bool = False):
    await message.answer(
        'Выбери действие:',
        reply_markup=get_inline_keyboard(
            ('Биржи', 'exchanges'),
            ('Кошельки', 'wallets'),
            ('Помощь', 'help'),
            ('Назад', 'back_menu'),
            ('Отмена', 'back_menu'),
            placeholder='Что вы хотели?',
            sizes=(2, 1, 2)
        ))
    if delete_original:
        await message.delete()


@start_router.message(CommandStart())
async def start_command(message: types.Message):
    await send_start_keyboard(message)
    await message.delete()


@start_router.callback_query(F.data == 'back_menu')
async def start_menu_callback(callback: types.CallbackQuery):
    await send_start_keyboard(callback.message, delete_original=True)
    await callback.answer()


@start_router.message(
        or_f(Command('menu'), F.text.lower().contains('меню')))
async def main_menu(message: types.Message):
    await send_menu_keyboard(message)
    await message.delete()


@start_router.callback_query(F.data == 'menu')
async def main_menu_callback(callback: types.CallbackQuery):
    await send_menu_keyboard(callback.message, delete_original=True)
    await callback.answer()


@start_router.callback_query(F.data == 'about_bot')
async def about_bot_callback(callback: types.CallbackQuery):
    await callback.message.edit_text('Это бот для работы с криптовалютами')
    await callback.answer()


@start_router.callback_query(F.data == 'contact_developer')
async def contact_developer_callback(callback: types.CallbackQuery):
    await callback.message.edit_text('Связь с разработчиком: @your_username')
    await callback.answer()


# @start_router.message()
# async def delete_message(message: types.Message):
#     await message.delete()
