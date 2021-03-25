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
        #print(time.strftime("%Y-%m-%d | %H:%M:%S ") + "Suites Page title = " + str(title))
        return title

    def failed_1_value_click(self):
        """Click on the "FAILED" value dropdown in the 1st row to see all failed test cases numbers"""
        self.visible_element_click(SuitesPageLocators.FAILED_1_DPDN)

    def suite_1st_link_click(self):
        """Click on the 1st test suite link to see all test cases in suite (open 'Cases' page)"""
        self.visible_element_click(SuitesPageLocators.SUITE_1_LNK)

    def calculate_test_cases_value_as_sum_of_test_cases(self):
        """Calculate number of test cases in test suite as sum of test cases in 1st row suite
            TEST_CASES_VALUE = PASSED_1_DPDN + FAILED_1_DPDN + BLOCKED_1_DPDN + NOT_EXECUTED_1_VALUE"""
        passed = int(self.visible_element_get_text(SuitesPageLocators.PASSED_1_DPDN))
        failed = int(self.visible_element_get_text(SuitesPageLocators.FAILED_1_DPDN))
        blocked = int(self.visible_element_get_text(SuitesPageLocators.BLOCKED_1_DPDN))
        not_executed = int(self.visible_element_get_text(SuitesPageLocators.NOT_EXECUTED_1_VALUE))
        t_c_sum_value = passed + failed + blocked + not_executed
        return t_c_sum_value














