from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from app.core import config

engine = create_async_engine(config.POSTGRES_URL, future=True)

async_session = async_sessionmaker(
    engine, expire_on_commit=False, autoflush=True
)
