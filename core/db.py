from sqlalchemy import Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import (declarative_base,
                            declared_attr,
                            Mapped,
                            mapped_column,
                            sessionmaker)

from core.config import settings


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.database_url)

async_session = AsyncSession(engine)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
