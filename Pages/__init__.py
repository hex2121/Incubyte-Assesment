
"""
This file marks the 'pages' directory as a Python package and
exposes the key page objects for easier import in test files.

Usage:
    from pages import HomePage, RegistrationPage, LoginPage, AccountPage
"""

from .base_page import BasePage            # Base class with common page functions
from .home_page import HomePage             # Home page object
from .registration_page import RegistrationPage  # Registration page object