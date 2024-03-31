import sqlalchemy as sa
from sqlalchemy import orm
from .base import DBBase


class HomeORM(DBBase):
    __tablename__ = 'home'
    
    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    date = sa.Column('date', sa.TIMESTAMP, nullable=False, unique=True)

    floors = orm.relationship('FloorORM', back_populates='home')

    def __repr__(self) -> str:
        return f'HomeORM(id={self.id}, date={self.date})'
