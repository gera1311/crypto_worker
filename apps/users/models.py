from typing import List

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.models import Base
from exchanges.models import CryptoExchange
from wallets.models import Wallet


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
