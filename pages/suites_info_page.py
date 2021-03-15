import time

from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import SuitesPageLocators
from locators.locators import BasePageLocators
from pages.base_page import BasePageElement
from utils.constants import DEFAULT_WAIT_TIME


class SuitesPage(BasePageElement):
    """
        Suites page for checking test results in test suits
    """

    def __init__(self, browser):
        super().__init__(browser)

    def load(self):
        self.browser.get(SuitesPageLocators.SUITES_URL)

    def get_title(self):
        title = self.browser.title
        print(time.strftime("%Y-%m-%d | %H:%M:%S ") + "Suites Page title = " + str(title))
        return title

    def failed_1_value_click(self):
        """Click on the "FAILED" value dropdown in the 1st row to see all failed test cases numbers"""
        self.visible_element_click(SuitesPageLocators.FAILED_1_DPDN)





