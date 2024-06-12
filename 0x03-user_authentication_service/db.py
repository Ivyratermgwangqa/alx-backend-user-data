#!/usr/bin/env python3
"""
Database interaction management.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from user import User
from typing import Optional

Base = declarative_base()


class DB:
    """
    DB class handles database interactions.

    Attributes:
        engine: SQLAlchemy engine instance.
        Session: SQLAlchemy session maker.
    """

    def __init__(self) -> None:
        """
        Initialize DB with a database URL.
        """
        self.engine = create_engine('sqlite:///mydatabase.db')
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.

        Args:
            email: The email of the user.
            hashed_password: The hashed password of the user.

        Returns:
            User: The created User object.
        """
        session = self.Session()
        new_user = User(email=email, hashed_password=hashed_password)
        session.add(new_user)
        session.commit()
        return new_user

    def find_user_by_email(self, email: str) -> User:
        """
        Find a user by email.

        Args:
            email: The email of the user.

        Returns:
            User: The found User object.
        """
        session = self.Session()
        return session.query(User).filter_by(email=email).first()

    def find_user_by_session_id(self, session_id: str) -> User:
        """
        Find a user by session ID.

        Args:
            session_id: The session ID.

        Returns:
            User: The found User object.
        """
        session = self.Session()
        return session.query(User).filter_by(session_id=session_id).first()

    def find_user_by_reset_token(self, reset_token: str) -> User:
        """
        Find a user by reset token.

        Args:
            reset_token: The reset token.

        Returns:
            User: The found User object.
        """
        session = self.Session()
        return session.query(User).filter_by(reset_token=reset_token).first()

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes.

        Args:
            user_id: The user ID.
            kwargs: The attributes to update.
        """
        session = self.Session()
        user = session.query(User).get(user_id)
        for key, value in kwargs.items():
            setattr(user, key, value)
        session.commit()
