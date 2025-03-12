from typing import List
from sqlalchemy import (DateTime,
                        ForeignKey,
                        Integer,
                        String,
                        func,
                        UniqueConstraint)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from bot.utils.encryption import encryption


class Base(DeclarativeBase):
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now())


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    wallets: Mapped[List['Wallet']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan'
    )
    exchanges: Mapped[List['CryptoExchange']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan'
    )


class CryptoExchange(Base):
    __tablename__ = 'crypto_exchange'
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
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


class Wallet(Base):
    __tablename__ = 'wallet'
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='wallets')
    address: Mapped[str] = mapped_column(String(255), unique=True)
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
