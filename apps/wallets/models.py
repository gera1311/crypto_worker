from sqlalchemy import ForeignKey, Integer, UniqueConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.models import Base
from users.models import User
from apps.utils import encryption


class Wallet(Base):
    __tablename__ = 'wallet'
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='wallets')
    address: Mapped[str] = mapped_column(String(255))
    withdraw_address: Mapped[str] = mapped_column(String(255), unique=True)
    __table_args__ = (UniqueConstraint('address',
                                       'withdraw_address',
                                       name='Адрес кошелька - Адрес вывода'))

    _private_key: Mapped[str] = mapped_column('private_key', String(255))

    @property
    def private_key(self) -> str:
        """Получение расшифрованного приватного ключа"""
        return encryption.decrypt(self._private_key)

    @private_key.setter
    def private_key(self, value: str):
        """Установка зашифрованного приватного ключа"""
        self._private_key = encryption.encrypt(value)