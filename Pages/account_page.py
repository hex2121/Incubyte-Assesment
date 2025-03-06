"""
AccountPage class representing the user's account page.
Contains methods to verify if the user is logged in and to log out.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage
from Locators.account_page_locators import *
from selenium.webdriver.support.ui import Select

class AccountPage(BasePage):
    def is_logged_in(self):
        """
        Verify if the user is logged in by checking the presence of the Welcome user text.

        :return: True if logged in, False otherwise
        """
        try:
            # If the Welcome user is visibile then user is logged in
            self.wait_for_visibility((By.XPATH, account_logged_in), timeout=20)
            return True
        except Exception:
            return False
    def is_created(self):
        """
                Verify if the user account is created in by checking the presence of the thank_you_for_registering text.

                :return: True if created , False otherwise
                """
        try:
            # If the thank_you_for_registering is displaying then account is successfully created
            self.wait_for_visibility((By.XPATH, thank_you_for_registering), timeout=20)
            return True
        except Exception:
            return False

