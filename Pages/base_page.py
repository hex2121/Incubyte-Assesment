from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
BasePage class that provides common functionality for all page objects.
Includes utility methods for waiting for elements to be clickable or visible.
"""
class BasePage:
    def __init__(self, driver):
        """
           Initialize the page object with a Selenium WebDriver instance.

           :param driver: Selenium WebDriver instance
        """
        self.driver = driver

    def wait_for_clickable(self, locator, timeout=10):
        """
            Wait until the element specified by locator is clickable.

            :param locator: Tuple (By.<METHOD>, 'value')
            :param timeout: Maximum time to wait (in seconds)
            :return: WebElement if clickable
        """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_visibility(self, locator, timeout=10):
        """
            Wait until the element specified by locator is visible.

            :param locator: Tuple (By.<METHOD>, 'value')
            :param timeout: Maximum time to wait (in seconds)
            :return: WebElement if visible
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
