from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart, or_f
from aiogram.types import ReplyKeyboardRemove

from keyboards.menu import menu_keyboard, start_keyboard

start_router = Router()

TEXT_START = ("привет! Я твой персональный помощник.")


@start_router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(
        f'{message.from_user.first_name}, {TEXT_START}',
        reply_markup=start_keyboard)
    await message.delete()


@start_router.message(
        or_f(Command('menu'), F.text.lower().contains('меню')))
async def main_menu_callback(message: types.CallbackQuery):
    await message.answer(
        'Выбери действие:', reply_markup=menu_keyboard)
    await message.answer(
        reply_markup=ReplyKeyboardRemove()
    )


@start_router.callback_query(F.data == 'about_bot')
async def about_bot_callback(callback: types.CallbackQuery):
    await callback.message.edit_text('Это бот для работы с криптовалютами')
    await callback.answer()


@start_router.callback_query(F.data == 'contact_developer')
async def contact_developer_callback(callback: types.CallbackQuery):
    await callback.message.edit_text('Связь с разработчиком: @your_username')
    await callback.answer()


@start_router.message()
async def delete_message(message: types.Message):
    await message.delete()
