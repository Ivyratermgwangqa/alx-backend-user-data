#!/usr/bin/env python3
"""
User model definition.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User class represents a user in the database.

    Attributes:
        id: Integer primary key.
        email: String unique email address.
        hashed_password: String hashed password.
        session_id: String session ID.
        reset_token: String reset password token.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
