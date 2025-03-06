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
        Verify if the user is logged in by checking the presence of the "Sign Out" link.

        :return: True if logged in, False otherwise
        """
        try:
            # If the "Sign Out" link is visible, the user is logged in
            self.wait_for_visibility((By.XPATH, account_logged_in))
            return True
        except Exception:
            return False

    def logout(self):
        """
        Log out the user by clicking the "Sign Out" link from the dropdown.
        """

        dropdown = self.driver.find_elements(By.XPATH, dropdown_button)
        dropdown = Select(dropdown)
        dropdown.select_by_visible_text("Sign Out")
        # logout_link = self.wait_for_clickable((By.LINK_TEXT, "Sign Out"))
        # logout_link.click()
