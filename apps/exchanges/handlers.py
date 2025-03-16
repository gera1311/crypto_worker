from aiogram import Router, types
from aiogram.filters import Command

from bot.keyboards import get_inline_keyboard


exchange_router = Router()


@exchange_router.message(Command('exchange'))
async def exchange_menu(message: types.Message):
    await message.answer(
        'Выберете действие',
        reply_markup=get_inline_keyboard(
            ('Массовый вывод', 'withdraw'),
            ('Вторая кнопка', 'second_func'),
            placeholder='Выберете действие',
            sizes=(2,)
        )
    )
    await message.delete()
