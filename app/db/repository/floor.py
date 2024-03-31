from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from . import BaseRepo
from .apart import Apart
from app.db.tables import FloorORM, ApartORM
from app.db.setup import async_session


class Floor(BaseRepo):
    ORM = FloorORM

    def __init__(self, id: int | None, n: int, home_id: int, session: AsyncSession = async_session):
        super().__init__(session)

        self.id: int | None = id
        self.n: int = n
        self.home_id: int = home_id

    def _get_orm(self) -> FloorORM:
        return FloorORM(id=self.id, n=self.n, home_id=self.home_id)
    
    @classmethod
    def get_repository(cls, orm: FloorORM, session: AsyncSession = async_session) -> Floor:
        id = orm.id if hasattr(orm, 'id') else None
        return Floor(id, orm.n, orm.home_id, session=session)

    @classmethod
    async def get(cls, id: int, session: AsyncSession = async_session) -> Floor:
        return await super().get(id, session=session)

    async def get_aparts(self) -> list[Apart]:
        async with self.session() as session:
            aparts = await session.scalars(
                sa.select(ApartORM)
                .where(ApartORM.floor_id == self.id)
            )
        return [Apart.get_repository(orm, self.session) for orm in aparts]
    
    def __repr__(self) -> str:
        return f'Floor(id={self.id}, n={self.n}, home_id={self.home_id})'

