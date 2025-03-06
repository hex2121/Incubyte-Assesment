
"""
LoginPage class representing the login page.
Contains methods to log in using the user's credentials.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage
from Locators.login_page_locators import *

class LoginPage(BasePage):
    def login(self, email, password):
        """
        Log in to the application using the provided credentials.

        :param email: User's email address
        :param password: User's password
        """
        # Wait for the email input field to be visible and enter the email
        email_field_object = self.wait_for_visibility((By.CSS_SELECTOR, email_field))
        email_field_object.send_keys(email)

        # Enter the password into the password field
        self.driver.find_element(By.XPATH, password_field).send_keys(password)

        # Wait for the login button to be clickable and click it to submit the login form
        login_button_object = self.wait_for_clickable((By.XPATH, login_button))
        login_button_object.click()
