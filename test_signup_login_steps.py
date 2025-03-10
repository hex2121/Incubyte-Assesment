# BDD test steps implementation for signup and login functionality
# This file contains the step definitions that map to the Gherkin scenarios
# in signup_login.feature. It follows the Given-When-Then pattern for behavior testing.

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from Pages.home_page import HomePage
from Pages.registration_page import RegistrationPage
from Pages.login_page import LoginPage
from Pages.account_page import AccountPage
from Config.config import website_link, firstname, lastname, email, password
import time
import openpyxl
import platform
import pytest

# Link to the feature file containing the Gherkin scenarios
scenarios('signup_login.feature')

@pytest.fixture
def driver():
    """Pytest fixture for Selenium WebDriver
    Sets up and tears down the browser instance for each test"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Initialize Excel workbook for test results logging
excel_path = "test_results.xlsx"
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append([
    "Test Case ID", "Test Case Name", "Description", "Preconditions", "Expected Result",
    "Status", "Execution Time (seconds)", "Start Time", "End Time", "Browser", "OS", "Error Message"
])

def log_result(test_id, test_name, description, preconditions, expected_result, status, execution_time, start_time, end_time, error_message=""):
    """Utility function to log test execution results in Excel
    Records test metadata, execution details, and results for reporting"""
    sheet.append([
        test_id, test_name, description, preconditions, expected_result,
        status, execution_time, start_time, end_time, "Chrome", platform.system(), error_message
    ])
    workbook.save(excel_path)

# Step Definitions for User Registration Scenario
@given('I am on the home page')
def on_home_page(driver):
    """Step: Navigate to the application home page
    Initializes the test environment and logs test start"""
    test_id = "TC_001"
    description = "User should be able to register successfully"
    preconditions = "None"
    expected_result = "User is redirected to their account page after login"
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    execution_start = time.time()
    try:
        # Navigate to the website
        driver.get(website_link)
        return HomePage(driver)
    except Exception as e:
        # Log test failure if navigation fails
        end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_result(test_id, "test_signup", description, preconditions, expected_result, "Fail", round(time.time() - execution_start, 2), start_time, end_time, str(e))
        raise e

@when('I click on create account')
def click_create_account(driver):
    """Step: Click the create account button
    Initiates the registration process"""
    home_page = HomePage(driver)
    home_page.click_create_account()

@when('I enter my registration details')
def enter_registration_details(driver):
    """Step: Fill in the registration form
    Enters user details from configuration"""
    registration_page = RegistrationPage(driver)
    registration_page.register_user(firstname, lastname, email, password)

@then('I should be successfully registered')
def verify_registration_success(driver):
    """Step: Verify successful registration
    Checks if user account is created and logs the result"""
    test_id = "TC_001"
    description = "User should be able to register successfully"
    preconditions = "None"
    expected_result = "User is redirected to their account page after login"
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    execution_start = time.time()
    try:
        # Verify account creation
        account_page = AccountPage(driver)
        assert account_page.is_created()
        end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_result(test_id, "test_signup", description, preconditions, expected_result, "Pass", round(time.time() - execution_start, 2), start_time, end_time)
    except Exception as e:
        # Log test failure if verification fails
        end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_result(test_id, "test_signup", description, preconditions, expected_result, "Fail", round(time.time() - execution_start, 2), start_time, end_time, str(e))
        raise e

# Step Definitions for User Login Scenario
@given('I am a registered user')
def registered_user(driver):
    """Step: Setup for login test
    Assumes user is already registered"""
    test_id = "TC_002"
    description = "User should be able to log in successfully"
    preconditions = "User has registered an account"
    expected_result = "User is redirected to their account page after login"
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    execution_start = time.time()
    try:
        # Navigate to the website for login
        driver.get(website_link)
        return HomePage(driver)
    except Exception as e:
        # Log test failure if navigation fails
        end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_result(test_id, "test_login", description, preconditions, expected_result, "Fail", round(time.time() - execution_start, 2), start_time, end_time, str(e))
        raise e

@when('I enter my login credentials')
def enter_login_credentials(driver):
    """Step: Perform login
    Enters login credentials and submits the form"""
    home_page = HomePage(driver)
    home_page.click_sign_in()
    login_page = LoginPage(driver)
    login_page.login_user(email, password)

@then('I should be successfully logged in')
def verify_login_success(driver):
    """Step: Verify successful login
    Checks if user is logged in and logs the result"""
    test_id = "TC_002"
    description = "User should be able to log in successfully"
    preconditions = "User has registered an account"
    expected_result = "User is redirected to their account page after login"
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    execution_start = time.time()
    try:
        # Verify successful login
        account_page = AccountPage(driver)
        assert account_page.is_logged_in()
        end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_result(test_id, "test_login", description, preconditions, expected_result, "Pass", round(time.time() - execution_start, 2), start_time, end_time)
    except Exception as e:
        # Log test failure if verification fails
        end_time = time.strftime("%Y-%m-%d %H:%M:%S")
        log_result(test_id, "test_login", description, preconditions, expected_result, "Fail", round(time.time() - execution_start, 2), start_time, end_time, str(e))
        raise e