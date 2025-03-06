"""
RegistrationPage class representing the registration page.
Contains methods to fill in the registration form and submit it.
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage
from Locators.registration_page_locators import *


class RegistrationPage(BasePage):
    def register_user(self, first_name, last_name, email, password):
        """
        Fill in the registration form and submit it.

        :param first_name: First name of the new user
        :param last_name: Last name of the new user
        :param email: Email address for registration
        :param password: Password for the account
        """
        # Wait for the first name field to be visible and enter the first name
        first_name_field_object = self.wait_for_visibility((By.CSS_SELECTOR, first_name_field))
        first_name_field_object.send_keys(first_name)

        # Enter the last name in the corresponding field
        self.driver.find_element(By.CSS_SELECTOR, last_name_field).send_keys(last_name)
        # Enter the email address
        self.driver.find_element(By.CSS_SELECTOR, email_address_field).send_keys(email)
        # Enter the password
        self.driver.find_element(By.XPATH, password_field).send_keys(password)
        # Confirm the password
        self.driver.find_element(By.CSS_SELECTOR, confirm_password_field).send_keys(password)

        # Wait for the "Create an Account" button to be clickable and then click it
        create_account_btn = self.wait_for_clickable((By.XPATH, create_an_account_button))
        create_account_btn.click()
