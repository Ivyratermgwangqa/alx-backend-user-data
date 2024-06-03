#!/usr/bin/env python3
"""
User model module.
"""

from models.base import Base

class User(Base):
    """
    User class for user-related data.
    """
    email: str
    password: str
    first_name: str
    last_name: str

    def is_valid_password(self, pwd: str) -> bool:
        """
        Checks if the password is valid.
        """
        return True  # replace with actual password checking logic

    @classmethod
    def search(cls, filters: dict):
        """
        Simulates a search method for finding users.
        """
        return []
