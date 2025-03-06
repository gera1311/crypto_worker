from typing import List
from sqlalchemy import DateTime, Float, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now())


class User(Base):
    __tablename__ = 'user_account'
    id: Mapped[int]
    crypto_exchange: Mapped[List['CryptoExchange']] = relationship(
        back_populates='user')
    wallet: Mapped[List['Wallet']] = relationship(back_populates='user')


class CryptoExchange(Base):
    __tablename__ = 'crypto_exchange'
    id: Mapped[int]
    user: Mapped['User'] = relationship(back_populates='crypto_exchange')
    public_key: Mapped[str]
    api_key: Mapped[str]
    api_secret: Mapped[str]
    pass_phrase: Mapped[str]


class Wallet(Base):
    __tablename__ = 'wallet'
    id: Mapped[int]
    user: Mapped['User'] = relationship(back_populates='wallet')
    address: Mapped[str]
    balance: Mapped[float]
