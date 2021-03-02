import time
from selenium.webdriver.common.by import By
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


    def trunner_lnk_click(self):
        "Click on Trunner_lnk"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        trunner_lnk = wait.until(EC.visibility_of_element_located(locators.SuiteManagerPageLocators.TRUNNER_LNK))
        trunner_lnk.click()

    def suites_option_select_by_index(self, n):
        "Check that user is able to select suites from option selector, where n-number of option"
        suite_selector_drp = Select(self.browser.find_element(*locators.SuiteManagerPageLocators.SUITE_SELECTOR_DPDN))
        suite_selector_drp.select_by_index(n)
        time.sleep(10)

    def suites_option_select_by_visible_text(self, element_text):
        "Check that user is able to select suites from option selector, where text-name of option"
        suite_selector_drp = Select(self.browser.find_element(*locators.SuiteManagerPageLocators.SUITE_SELECTOR_DPDN))
        suite_selector_drp.select_by_visible_text(element_text)
        time.sleep(10)

    def tc_checkbox_option_click(self, n):
        "Click on TC checkbox from dropdown"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        tc_checkbox = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".test_case_row:nth-of-type(" + str(n) + ") .check-row")))
        tc_checkbox.click()

    def get_id_tc_value(self, n):
        "Get id of test case"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        id = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".table .test_case_row:nth-of-type(" + str(n) + ") .tcid")))
        return int(id.text)

    def get_tc_title(self, n):
        "Get test case title"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        tc_title = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".test_case_row:nth-of-type(" + str(n) + ") td:last-child")))
        return tc_title.text

    def add_modal_window(self):
        "Opening modal 'Add to Suite' window by clicking on +Add button"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        add_lnk = wait.until(EC.visibility_of_element_located(locators.SuiteManagerPageLocators.ADD_CASE_TO_SUITE_BTN))
        add_lnk.click()

    def get_tc_title_in_modal_add_window(self):
        "Get test case name in modal window 'Add to Suite'"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        test_case_name = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "tbody>tr>td:nth-of-type(" + str(n) + ")")))
        return test_case_name.text

    def click_add_button(self):
        "Click on  button 'Add Test Cases' in modal window 'Add to Suite'"
        add_button = self.browser.find_element(*locators.SuiteManagerPageLocators.ADD_TC_BUTTON_MODALW)
        add_button.click()

    def click_checkbox_in_modal_add_window(self):
        "Select checkbox of test cases in 'Add Test Cases' modal window"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        new = wait.until(EC.element_to_be_clickable(locators.SuiteManagerPageLocators.CHECKBOX_TC_MODALW))
        new.click()

    def close_add_test_modal_window(self):
        "Close 'Add to Suite' modal window"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        close_button = wait.until(
            EC.element_to_be_clickable(locators.SuiteManagerPageLocators.CLOSE_ADD_TEST_CASE_MODALW))
        close_button.click()

    def click_delete_button(self):
        "Click on the  button '-Delete'"
        delete_button = self.browser.find_element(*locators.SuiteManagerPageLocators.DELETE_CASE_FROM_SUITE_BTN)
        delete_button.click()

    def get_text_from_alert(self):
        "Getting text from alert dialog"
        WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.alert_is_present())
        alert = self.browser.switch_to_alert()
        alert_text = alert.text
        return alert_text

    def handling_alert(self):
        "Alert acceptation"
        WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.alert_is_present())
        alert = self.browser.switch_to_alert()
        alert.accept()

    def input_text_in_search_field(self, text):
        """Input some text into 'Search for test case' textbox on Suite Manager Page"""
        WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.visibility_of_all_elements_located(SuiteManagerPageLocators.TEST_CASE_TITLE))
        tbx = WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.element_to_be_clickable(SuiteManagerPageLocators.SEARCH_FIELD))
        tbx.send_keys(text, Keys.RETURN)

    def click_create_suite_button(self):
        "Click on the  button 'Create_suite'"
        create_suite_button = WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.element_to_be_clickable(SuiteManagerPageLocators.CREATE_SUITE_DPDN))
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        create_suite_button.click()

    def create_from_ADO_query(self):
        "Select option 'Create from ADO_query' in the Create suite dropdown"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        create_from_ado = wait.until(EC.element_to_be_clickable(locators.SuiteManagerPageLocators.FROM_ADO_QUERY_OPT))
        create_from_ado.click()

    def create_empty_suite(self):
        "Select option 'Empty suite' in the Create suite dropdown"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        create_empty_suite = wait.until(EC.element_to_be_clickable(locators.SuiteManagerPageLocators.EMPTY_SUITE_OPT))
        create_empty_suite.click()

    def create_from_existing_suite(self):
        "Select option 'From existing suite' in the Create suite dropdown"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        create_from_exist_suite = wait.until(EC.element_to_be_clickable(locators.SuiteManagerPageLocators.FROM_EXIST_SUITE_OPT))
        create_from_exist_suite.click()

    def close_create_from_ADO_query_window(self):
        "Close 'Create Test Suite from ADO Query' window"
        close_icons= self.browser.find_elements(By.CSS_SELECTOR, "span[aria-hidden='true']")
        close_icons[1].click()

    def close_create_empty_suite_window(self):
        "Close 'create Empty suite' window "
        close_icons = self.browser.find_elements(By.CSS_SELECTOR, "span[aria-hidden='true']")
        close_icons[2].click()

    def close_copy_test_suite_window(self):
        "Close 'Copy Suite' window"
        close_icons = self.browser.find_elements(By.CSS_SELECTOR, "span[aria-hidden='true']")
        close_icons[3].click()