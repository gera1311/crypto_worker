from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from apps.utils.encryption import encryption
from core.db import Base

if TYPE_CHECKING:
    # Импорты только для проверки типов, не выполняются при запуске
    from apps.users.models import User


class CryptoExchange(Base):
    name: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='exchanges')

    _api_key: Mapped[str] = mapped_column('api_key', String(255))
    _api_secret: Mapped[str] = mapped_column('api_secret', String(255))
    _pass_phrase: Mapped[str] = mapped_column('pass_phrase', String(255))

    @property
    def api_key(self) -> str:
        """Получение расшифрованного API ключа"""
        return encryption.decrypt(self._api_key)

    @api_key.setter
    def api_key(self, value: str):
        """Установка зашифрованного API ключа"""
        self._api_key = encryption.encrypt(value)

    @property
    def api_secret(self) -> str:
        """Получение расшифрованного API секрета"""
        return encryption.decrypt(self._api_secret)

    @api_secret.setter
    def api_secret(self, value: str):
        """Установка зашифрованного API секрета"""
        self._api_secret = encryption.encrypt(value)

    @property
    def pass_phrase(self) -> str:
        """Получение расшифрованной pass phrase"""
        return encryption.decrypt(self._pass_phrase)

    @pass_phrase.setter
    def pass_phrase(self, value: str):
        """Установка зашифрованной pass phrase"""
        self._pass_phrase = encryption.encrypt(value)