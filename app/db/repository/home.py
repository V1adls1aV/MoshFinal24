from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from datetime import datetime

from .base import BaseRepo
from .floor import Floor
from app.db.tables import HomeORM, FloorORM
from app.db.setup import async_session


class Home(BaseRepo):
    ORM = HomeORM

    def __init__(self, id: int | None, date: datetime, session: AsyncSession = async_session):
        super().__init__(session)

        self.id: int | None = id
        self.date: datetime = date

    def _get_orm(self) -> HomeORM:
        return HomeORM(id=self.id, date=self.date)
    
    @classmethod
    def get_repository(cls, orm: HomeORM, session: AsyncSession = async_session) -> Home:
        id = orm.id if hasattr(orm, 'id') else None
        return Home(id, orm.date, session=session)

    @classmethod
    async def get(cls, id: int, session: AsyncSession = async_session) -> Home:
        return await super().get(id, session=session)

    @classmethod
    async def get_by_date(cls, date: datetime, session: AsyncSession = async_session) -> Home:
        async with session() as session:
            result = await session.execute(
                sa.select(HomeORM)
                .where(HomeORM.date == date)
            )
            return cls.get_repository(result.scalar())

    async def get_floors(self) -> list[Floor]:
        async with self.session() as session:
            floors = await session.scalars(
                sa.select(FloorORM)
                .where(FloorORM.home_id == self.id)
            )
        return [Floor.get_repository(orm, self.session) for orm in floors]
    
    def __repr__(self) -> str:
        return f'Home(id={self.id}, date={self.date})'
