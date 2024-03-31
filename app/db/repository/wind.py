from __future__ import annotations
from sqlalchemy.ext.asyncio import AsyncSession

from . import BaseRepo
from .wind import Wind
from app.db.tables import WindORM
from app.db.setup import async_session


class Wind(BaseRepo):
    ORM = WindORM

    def __init__(self, id: int | None, light: int, apart_id: int, session: AsyncSession = async_session):
        super().__init__(session)

        self.id: int | None = id
        self.light: int = light
        self.apart_id: int = apart_id

    def _get_orm(self) -> WindORM:
        return WindORM(id=self.id, light=self.light, apart_id=self.apart_id)
    
    @classmethod
    def get_repository(cls, orm: WindORM, session: AsyncSession = async_session) -> Wind:
        id = orm.id if hasattr(orm, 'id') else None
        return WindORM(id, orm.light, orm.apart_id, session=session)

    @classmethod
    async def get(cls, id: int, session: AsyncSession = async_session) -> Wind:
        return await super().get(id, session=session)
    
    def __repr__(self) -> str:
        return f'Wind(id={self.id}, light={self.light}, apart_id={self.apart_id})'
