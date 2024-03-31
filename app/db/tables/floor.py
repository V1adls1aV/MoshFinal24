import sqlalchemy as sa
from sqlalchemy import orm
from .base import DBBase


class FloorORM(DBBase):
    __tablename__ = 'floor'
    
    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    n = sa.Column('n', sa.Integer, nullable=False)
    home_id = sa.Column('home_id', sa.ForeignKey('home.id'))

    home = orm.relationship('HomeORM', back_populates='floors')
    aparts = orm.relationship('ApartORM', back_populates='floor')

    def __repr__(self) -> str:
        return f'FloorORM(id={self.id}, n={self.n}, home_id={self.home_id})'
