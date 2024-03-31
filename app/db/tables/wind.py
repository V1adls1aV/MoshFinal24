import sqlalchemy as sa
from sqlalchemy import orm
from .base import DBBase


class WindORM(DBBase):
    __tablename__ = 'wind'
    
    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    light = sa.Column('n', sa.Integer, nullable=False)
    apart_id = sa.Column('apart_id', sa.ForeignKey('apart.id'))

    apart = orm.relationship('ApartORM', back_populates='winds')

    def __repr__(self) -> str:
        return f'WindORM(id={self.id}, light={self.light}, apart_id={self.apart_id})'
