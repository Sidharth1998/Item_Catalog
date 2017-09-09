import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # user's table

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Categories(Base):
    __tablename__ = 'categories'
    # categories table

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    items = relationship('Item', cascade='all, delete-orphan')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Item(Base):
    __tablename__ = 'items'
    # items table

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    description = Column(String(500))
    categories_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship(Categories)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'id': self.id,
            'description': self.description,
        }


engine = create_engine('sqlite:///catalogsusers.db')


Base.metadata.create_all(engine)
