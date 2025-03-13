from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from core.db import Base
from apps.exchanges.models import CryptoExchange

if TYPE_CHECKING:
    # Импорты только для проверки типов, не выполняются при запуске
    from wallets.models import Wallet


class User(Base):
    wallets: Mapped[List['Wallet']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan'
    )
    exchanges: Mapped[List['CryptoExchange']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan'
    )
