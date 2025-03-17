from aiogram import Router, types, F
from aiogram.filters import Command

from bot.keyboards import get_inline_keyboard


exchange_router = Router()


EXCHANGE_KEYBOARD = get_inline_keyboard(
    ('Вывод средств', 'withdraw'),
    ('Управление', 'config'),
    ('Назад', 'back'),
    ('Отмена', 'cancel'),
    placeholder='Информация об аккаунте',
    sizes=(2, 2)
)


@exchange_router.message(Command('exchanges'))
async def exchange_menu(message: types.Message):
    await message.answer(
        'Выберете действие',
        reply_markup=EXCHANGE_KEYBOARD
    )
    await message.delete()


@exchange_router.callback_query(F.data == 'exchanges')
async def exchange_menu_callback(callback: types.CallbackQuery):
    await callback.message.answer(
        'Выберете действие', reply_markup=EXCHANGE_KEYBOARD
    )
    await callback.message.delete()
    await callback.answer()
