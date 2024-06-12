#!/usr/bin/env python3
"""
Authentication management.
"""

import bcrypt
from db import DB
from user import User
from typing import Optional
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound

class Auth:
    """
    Auth class handles authentication processes.

    Attributes:
        db: An instance of the DB class.
    """

    def __init__(self) -> None:
        """
        Initialize Auth with a DB instance.
        """
        self.db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with an email and password.

        Args:
            email: The email of the user.
            password: The password of the user.

        Returns:
            User: The created User object.
        """
        try:
            self.db.find_user_by_email(email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            return self.db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate login credentials.

        Args:
            email: The email of the user.
            password: The password of the user.

        Returns:
            bool: True if credentials are valid, False otherwise.
        """
        try:
            user = self.db.find_user_by_email(email)
            return bcrypt.checkpw(password.encode(), user.hashed_password.encode())
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Create a session ID for a user.

        Args:
            email: The email of the user.

        Returns:
            str: The session ID.
        """
        user = self.db.find_user_by_email(email)
        session_id = str(uuid4())
        self.db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """
        Retrieve a user by session ID.

        Args:
            session_id: The session ID.

        Returns:
            Optional[User]: The user associated with the session ID.
        """
        if session_id is None:
            return None
        try:
            user = self.db.find_user_by_session_id(session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy a user's session.

        Args:
            user_id: The user ID.
        """
        self.db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a reset password token.

        Args:
            email: The email of the user.

        Returns:
            str: The reset password token.
        """
        user = self.db.find_user_by_email(email)
        reset_token = str(uuid4())
        self.db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update a user's password using a reset token.

        Args:
            reset_token: The reset token.
            password: The new password.
        """
        try:
            user = self.db.find_user_by_reset_token(reset_token)
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            self.db.update_user(user.id, hashed_password=hashed_password, reset_token=None)
        except NoResultFound:
            raise ValueError("Invalid reset token")
