from locators.locators import RunTestPageLocators
from pages.base_page import BasePageElement
from utils.constants import DEFAULT_WAIT_TIME


class RunTestPage(BasePageElement):
    """
        Run page for running test cases (+ edit and create new bug options)
    """

    def __init__(self, browser):
        super().__init__(browser)

    def get_title(self):
        """Return title of the page"""
        title = self.browser.title
        #print(f"Run Test Page title = {str(title)}")
        return title

    def save_btn_click(self):
        """Click on 'Save' button on 'Run Test' page"""
        self.visible_element_click(RunTestPageLocators.SAVE_BTN)

    def save_and_close_btn_click(self):
        """Click on 'Save and Close' button on 'Run Test' page"""
        self.visible_element_click(RunTestPageLocators.SAVE_AND_CLOSE_BTN)

    def report_a_bug_btn_click(self):
        """Click on 'Report a Bug' button on 'Run Test' page"""
        self.visible_element_click(RunTestPageLocators.REPORT_BUG_BTN)

    def back_to_suite_btn_click(self):
        """Click on 'Back to Suite' button on 'Run Test' page"""
        self.visible_element_click(RunTestPageLocators.BACK_TO_SUITE_BTN)

    def info_icon_click(self):
        """Click on 'I' icon on 'Run Test' page"""
        self.visible_element_click(RunTestPageLocators.REPORT_BUG_BTN)

    def test_status_dpdn_click(self):
        """Click on test case status dropdown on 'Run Test' page"""
        self.visible_element_click(RunTestPageLocators.TC_STATUS_DPDN)

    def get_test_status(self):
        """Get the Status of test case"""
        status = self.visible_element_get_value(RunTestPageLocators.TC_STATUS_OPT)
        return status

    def get_test_case_name(self):
        """Get the test case title from 'Run Test' page"""
        name = self.visible_element_get_text(RunTestPageLocators.TC_TITLE)
        return name

    def passed_btn_1_step_click(self):
        """Click on 'Passed' button for the 1st step on 'Run Test' page"""
        self.visible_element_click(RunTestPageLocators.TC_1ST_STEP_PASSED_STATUS)

    def failed_btn_1_step_click(self):
        """Click on 'Failed' button for the 1st step on 'Run Test' page"""
        self.visible_element_click(RunTestPageLocators.TC_1ST_STEP_FAILED_STATUS)


