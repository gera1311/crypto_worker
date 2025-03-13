"""Импорты класса Base и всех моделей для Alembic."""
from core.db import Base # noqa
from apps.exchanges.models import CryptoExchange # noqa
from apps.users.models import User # noqa
from apps.wallets.models import Wallet # noqa
