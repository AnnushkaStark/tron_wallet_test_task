from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql.sqltypes import ARRAY, Integer, String

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./wallet.db"

async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True
)


async_session = async_sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    type_annotation_map = {  # noqa: RUF012
        list: ARRAY,
        list[str]: ARRAY(String),
        list[int]: ARRAY(Integer),
    }


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
