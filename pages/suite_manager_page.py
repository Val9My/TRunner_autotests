import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators
from locators.locators import SuiteManagerPageLocators
from pages.base_page import BasePageElement
from utils.constants import DEFAULT_WAIT_TIME


class SuiteManagerPage(BasePageElement):

    def __init__(self, browser):
        super().__init__(browser)

    def load(self):
        super().load(SuiteManagerPageLocators.SUITE_MANAGER_PAGE_URL)

    def trunner_lnk_click(self):
        "Click on Trunner_lnk"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        trunner_lnk = wait.until(EC.visibility_of_element_located(locators.SuiteManagerPageLocators.TRUNNER_LNK))
        trunner_lnk.click()

    def suites_option_select_by_index(self, n):
        'Check that user is able to select suites from option selector, where n-number of option'
        suite_selector_drp = Select(self.browser.find_element(*locators.SuiteManagerPageLocators.SUITE_SELECTOR_DPDN))
        suite_selector_drp.select_by_index(n)
        time.sleep(10)

    def suites_option_select_by_visible_text(self, element_text):
        'Check that user is able to select suites from option selector, where text-name of option'
        suite_selector_drp = Select(self.browser.find_element(*locators.SuiteManagerPageLocators.SUITE_SELECTOR_DPDN))
        suite_selector_drp.select_by_visible_text(element_text)
        time.sleep(10)

    def tc_checkbox_option_click(self, n):
        'click on TC checkbox'
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        tc_checkbox = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".test_case_row:nth-of-type(" + str(n) + ") .check-row")))
        tc_checkbox.click()

    def get_id_tc_value(self, n):
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        id = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".table .test_case_row:nth-of-type(" + str(n) + ") .tcid")))
        return int(id.text)

    def get_tc_title(self, n):
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        tc_title = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".test_case_row:nth-of-type(" + str(n) + ") td:last-child")))
        return tc_title.text
