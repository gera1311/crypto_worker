from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, or_f
from keyboards.menu import menu_keyboard, start_keyboard

start_router = Router()


@start_router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! "
                         f"Я твой персональный помощник.",
                         reply_markup=start_keyboard)


@start_router.message(or_f(Command('menu'), F.text.lower() == 'меню'))
async def menu_command(message: types.Message):
    await message.answer('Выбери действие:', reply_markup=menu_keyboard)
