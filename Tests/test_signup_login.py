"""
Test suite for the signup and login functionality using Selenium and pytest.
This test follows a Behavior-Driven Development (BDD) style:
    Given a new user with valid details,
    When the user registers, logs out, and logs back in,
    Then the user should be successfully logged in.
"""

import pytest
import time
import openpyxl
import platform
from selenium import webdriver
from Pages.home_page import HomePage
from Pages.registration_page import RegistrationPage
from Pages.login_page import LoginPage
from Pages.account_page import AccountPage
from Config.config import website_link, firstname, lastname, email, password

# Initialize Excel workbook and sheet
excel_path = "test_results.xlsx"
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append([
    "Test Case ID", "Test Case Name", "Description", "Preconditions", "Expected Result",
    "Status", "Execution Time (seconds)", "Start Time", "End Time", "Browser", "OS", "Error Message"
])

@pytest.fixture
def driver():
    """
    Pytest fixture to initialize and tear down the Selenium WebDriver.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def log_result(test_id, test_name, description, preconditions, expected_result, status, execution_time, start_time, end_time, error_message=""):
    """Function to log test results in Excel"""
    sheet.append([
        test_id, test_name, description, preconditions, expected_result,
        status, execution_time, start_time, end_time, "Chrome", platform.system(), error_message
    ])
    workbook.save(excel_path)

def test_signup(driver):
    """
    Test scenario:
    Given a new user with valid registration details,
    When the user registers,
    Then they should be successfully registered.
    """
    test_id = "TC_001"
    description = "User should be able to register successfully"
    preconditions = "None"
    expected_result = "User is redirected to their account page after login"
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    execution_start = time.time()
    try:
        driver.get(website_link)
        home_page = HomePage(driver)
        home_page.click_create_account()
        registration_page = RegistrationPage(driver)
        registration_page.register_user(firstname, lastname, email, password)
        end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_result(test_id, "test_signup", description, preconditions, expected_result, "Pass", round(time.time() - execution_start, 2), start_time, end_time)
    except Exception as e:
        end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_result(test_id, "test_signup", description, preconditions, expected_result, "Fail", round(time.time() - execution_start, 2), start_time, end_time, str(e))
        raise e

def test_login(driver):
    """
    Test scenario:
    Given a registered user,
    When they log in with correct credentials,
    Then they should be successfully logged in.
    """
    test_id = "TC_002"
    description = "User should be able to log in successfully"
    preconditions = "User has registered an account"
    expected_result = "User gets Welcome Username in the Dropdown"
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    execution_start = time.time()
    try:
        driver.get(f'{website_link}customer/account/login/')
        login_page = LoginPage(driver)
        login_page.login_user(email, password)
        account_page = AccountPage(driver)
        assert account_page.is_logged_in()
        end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_result(test_id, "test_login", description, preconditions, expected_result, "Pass", round(time.time() - execution_start, 2), start_time, end_time)
    except Exception as e:
        end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_result(test_id, "test_login", description, preconditions, expected_result, "Fail", round(time.time() - execution_start, 2), start_time, end_time, str(e))
        raise e
