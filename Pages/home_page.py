from selenium.webdriver.common.by import By
from .base_page import BasePage
from Locators.home_page_locators import *

"""
HomePage class representing the home page of the application.
Contains methods to interact with elements on the home page.
"""

class HomePage(BasePage):
    def click_create_account(self):
        """
        Click on the "Create an Account" link to navigate to the registration page.
        """
        # Wait for the "Create an Account" link to be clickable
        create_account_link = self.wait_for_clickable((By.LINK_TEXT, "Create an Account"))
        create_account_link.click()
