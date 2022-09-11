from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column('address', String(120), nullable=True)
    phone = relationship('Phone', back_populates='user', cascade="all, delete-orphan")
    email = relationship('Email', back_populates='user', cascade='all, delete-orphan')


class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone_number = Column('phone_number', String(20), nullable=False)
    user_id = Column('user_id', Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='phone')


class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    email = Column('email', String(120), nullable=False)
    user_id = Column('user_id', Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='email')