from locators.locators import CasesPageLocators
from pages.base_page import BasePageElement
from utils.constants import DEFAULT_WAIT_TIME


class CasesPage(BasePageElement):
    """
        Test Cases page selected in one suite
    """

    def __init__(self, browser):
        super().__init__(browser)

    def get_title(self):
        """return title of the page"""
        title = self.browser.title
        #print(f"Cases Page title = {str(title)}")
        return title

    def load(self, url):
        self.browser.get(url)

    def run_test_btn_click(self):
        """Click on 'Run Test' button on 'Cases' page"""
        self.visible_element_click(CasesPageLocators.RUN_TEST_BTN)

    def click_first_case(self):
        """Click on first case to select"""
        self.visible_element_click(CasesPageLocators.ACTIVE_1ST_ROW)

    def get_first_case_name(self):
        """Get 1st test case title"""
        name = self.visible_element_get_text(CasesPageLocators.CASE_NAME)
        return name

    def get_first_case_tester_name(self):
        """Get 1st test case tester name"""
        tester_name = self.visible_element_get_text(CasesPageLocators.TESTER_NAME)
        return tester_name

    def get_first_case_status(self):
        """Get 1st test case tester name"""
        case_status = self.visible_element_get_text(CasesPageLocators.CASE_STATE)
        return case_status

