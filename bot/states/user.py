from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    """Состояния пользователя"""
    main_menu = State()  # Главное меню
    exchanges_menu = State()  # Меню бирж
    attaching_exchange = State()  # Процесс привязки биржи
    detaching_exchange = State()  # Процесс отвязки биржи
    mass_withdrawal = State()  # Процесс массового вывода
