from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from .base import BaseRepo
from .wind import Wind
from app.db.tables import ApartORM, WindORM
from app.db.setup import async_session


class Apart(BaseRepo):
    ORM = ApartORM

    def __init__(self, id: int | None, n: int, floor_id: int, session: AsyncSession = async_session):
        super().__init__(session)

        self.id: int | None = id
        self.n: int = n
        self.floor_id: int = floor_id

    def _get_orm(self) -> ApartORM:
        return ApartORM(id=self.id, n=self.n, floor_id=self.floor_id)
    
    @classmethod
    def get_repository(cls, orm: ApartORM, session: AsyncSession = async_session) -> Apart:
        id = orm.id if hasattr(orm, 'id') else None
        return Apart(id, orm.n, orm.floor_id, session=session)

    @classmethod
    async def get(cls, id: int, session: AsyncSession = async_session) -> Apart:
        return await super().get(id, session=session)

    async def get_winds(self) -> list[Wind]:
        async with self.session() as session:
            winds = await session.scalars(
                sa.select(WindORM)
                .where(WindORM.apart_id == self.id)
            )
        return [Wind.get_repository(orm, self.session) for orm in winds]
    
    def __repr__(self) -> str:
        return f'Apart(id={self.id}, n={self.n}, floor_id={self.floor_id})'
