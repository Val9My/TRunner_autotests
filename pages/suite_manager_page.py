import time
from selenium.webdriver.common.keys import Keys
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

    def suites_option_select_by_index(self, n):
        """Check that user is able to select suites from option selector, where n-number of option"""
        suite_selector_drp = Select(self.browser.find_element(*locators.SuiteManagerPageLocators.SUITE_SELECTOR_DPDN))
        suite_selector_drp.select_by_index(n)
        time.sleep(10)

    def suites_option_select_by_visible_text(self, element_text):
        """Check that user is able to select suites from option selector, where text-name of option"""
        suite_selector_drp = Select(self.browser.find_element(*locators.SuiteManagerPageLocators.SUITE_SELECTOR_DPDN))
        suite_selector_drp.select_by_visible_text(element_text)
        time.sleep(10)

    def tc_checkbox_option_click(self, n):
        """Click on TC checkbox from dropdown"""
        self.visible_element_click(locators.SuiteManagerPageLocators.USE_TC_CHKBX,n)

    def get_id_tc_value(self, n):
        """Get id of test case"""
        id_text = self.visible_element_get_text(locators.SuiteManagerPageLocators.ID_TC_VALUE, n)
        return id_text

    def get_tc_title(self, n):
        """Get test case title"""
        tc_title = self.visible_element_get_text(locators.SuiteManagerPageLocators.TEST_CASE_TITLE, n)
        return tc_title

    def add_modal_window(self):
        """Opening modal 'Add to Suite' window by clicking on +Add button"""
        self.visible_element_click(locators.SuiteManagerPageLocators.ADD_CASE_TO_SUITE_BTN)

    def get_tc_title_in_modal_add_window(self):
        """Get test case name in modal window 'Add to Suite'"""
        tc_title = self.visible_element_get_text(locators.SuiteManagerPageLocators.TEST_CASE_TITLE_IN_ADD_MODAL_WINDOW)
        return tc_title

    def click_add_button(self):
        """Click on 'Add Test Cases' button  in modal window 'Add to Suite'"""
        self.visible_element_click(locators.SuiteManagerPageLocators.ADD_TC_BUTTON_MODALW)

    def click_checkbox_in_modal_add_window(self):
        """Select checkbox of test cases in 'Add Test Cases' modal window"""
        self.visible_element_click(locators.SuiteManagerPageLocators.CHECKBOX_TC_MODALW)

    def close_add_test_modal_window(self):
        """Close 'Add to Suite' modal window"""
        self.visible_element_click(locators.SuiteManagerPageLocators.CLOSE_ADD_TEST_CASE_MODALW)

    def click_delete_button(self):
        """Click on the '-Delete' button """
        self.visible_element_click(locators.SuiteManagerPageLocators.DELETE_CASE_FROM_SUITE_BTN)

    def input_text_in_search_field(self, text):
        """Input some text into 'Search for test case' textbox on Suite Manager Page"""
        WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.visibility_of_all_elements_located(SuiteManagerPageLocators.TEST_CASE_TITLE))
        tbx = WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.element_to_be_clickable(SuiteManagerPageLocators.SEARCH_FIELD))
        tbx.send_keys(text, Keys.RETURN)

    def backspace_in_search_field(self):
        """Clear text in 'Search for test case' textbox on Suite Manager Page"""
        tbx = WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(
            EC.element_to_be_clickable(SuiteManagerPageLocators.SEARCH_FIELD))
        tbx.send_keys(Keys.BACKSPACE)

    def click_create_suite_button(self):
        """Click on the  button 'Create_suite'"""
        create_suite_button = WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.element_to_be_clickable(SuiteManagerPageLocators.CREATE_SUITE_DPDN))
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        create_suite_button.click()

    def create_from_ado_query(self):
        """Select option 'Create from ADO_query' in the Create suite dropdown"""
        self.visible_element_click(locators.SuiteManagerPageLocators.FROM_ADO_QUERY_OPT)

    def create_empty_suite(self):
        """Select option 'Empty suite' in the Create suite dropdown"""
        self.visible_element_click(locators.SuiteManagerPageLocators.EMPTY_SUITE_OPT)

    def create_from_existing_suite(self):
        """Select option 'From existing suite' in the Create suite dropdown"""
        self.visible_element_click(locators.SuiteManagerPageLocators.FROM_EXIST_SUITE_OPT)

    def close_create_from_ado_query_window(self):
        """Close 'Create Test Suite from ADO Query' window"""
        self.visible_element_click(locators.SuiteManagerPageLocators.CLOSE_ICON,2)

    def close_create_empty_suite_window(self):
        """Close 'create Empty suite' window """
        self.visible_element_click(locators.SuiteManagerPageLocators.CLOSE_ICON,3)

    def close_copy_test_suite_window(self):
        """Close 'Copy Suite' window"""
        self.visible_element_click(locators.SuiteManagerPageLocators.CLOSE_ICON,4)

