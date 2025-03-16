from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard(
        *buttons: tuple[str, str],
        sizes: tuple[int] = (2,),
        placeholder: str = None,
        url_buttons: tuple[tuple[str, str]] = None
):
    '''
    Parameters request_contact and request_location must be as indexes
    of btns args for buttons you need.
    Example:
    get_keyboard(
            "Меню",
            "О магазине",
            "Варианты оплаты",
            "Варианты доставки",
            "Отправить номер телефона"
            placeholder="Что вас интересует?",
            request_contact=4,
            sizes=(2, 2, 1)
        )
    '''
    keyboard = InlineKeyboardBuilder()

    for text, callback_data in buttons:
        keyboard.add(InlineKeyboardButton(text=text,
                                          callback_data=callback_data))

    if url_buttons:
        for text, url in url_buttons:
            keyboard.add(InlineKeyboardButton(text=text,
                                              url=url))

    return keyboard.adjust(*sizes).as_markup(
        resize_keyboard=True,
        input_field_placeholder=placeholder
    )
