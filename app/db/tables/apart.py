import sqlalchemy as sa
from sqlalchemy import orm
from .base import DBBase


class ApartORM(DBBase):
    __tablename__ = 'apart'
    
    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    n = sa.Column('n', sa.Integer, nullable=False)
    floor_id = sa.Column('floor_id', sa.ForeignKey('floor.id'))

    floor = orm.relationship('FloorORM', back_populates='aparts')
    winds = orm.relationship('WindORM', back_populates='apart')

    def __repr__(self) -> str:
        return f'ApartORM(id={self.id}, n={self.n}, floor_id={self.floor_id})'
