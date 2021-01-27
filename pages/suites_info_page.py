import time

from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import SuitesPageLocators
from utils.constants import DEFAULT_WAIT_TIME


class SuitesPage:
    """
        Suites page for checking test results in test suits
    """

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(SuitesPageLocators.SUITES_URL)

    def get_title(self):
        title = self.browser.title
        print(time.strftime("%Y-%m-%d | %H:%M:%S ") + "Suites Page title = " + str(title))
        return title

    def failed_1_value_click(self):
        """Click on the "FAILED" value dropdown in the 1st row to see all failed test cases numbers"""
        try:
            wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
            failed_t_c = wait.until(EC.element_to_be_clickable(SuitesPageLocators.FAILED_1_DPDN))
            try:
                failed_t_c.click()
            except ElementNotVisibleException:
                failed_t_c = wait.until(EC.visibility_of_element_located(SuitesPageLocators.FAILED_1_DPDN))
                failed_t_c.click()
        except TimeoutException:
            print("Failed T-C column not found in suites")

    def is_element_seen(self, locator):
        """Check that element seen on page"""
        try:
            element = WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException as e:
            print(locator, " - element is not seen timeout error", e)
            return False

    def about_btn_click(self):
        """Click on the 'About' button """
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        about = wait.until(EC.visibility_of_element_located(SuitesPageLocators.ABOUT_LNK))
        about.click()