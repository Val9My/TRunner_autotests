from selenium.webdriver.common.by import By

from locators.locators import CasesPageLocators
from pages.base_page import BasePageElement


class CasesPage(BasePageElement):
    """
        Test Cases page selected in one suite
    """

    def __init__(self, browser):
        super().__init__(browser)

    def get_title(self):
        """return title of the page"""
        title = self.browser.title
        # print(f"Cases Page title = {str(title)}")
        return title

    def load(self, url):
        self.browser.get(url)

    def run_test_btn_click(self):
        """Click on 'Run Test' button on 'Cases' page"""
        self.visible_element_click(CasesPageLocators.RUN_TEST_BTN)

    def click_first_case(self):
        """Click on first case to select"""
        self.visible_element_click(CasesPageLocators.ACTIVE_1ST_ROW)

    def click_mb3_first_case(self):
        """Click MB3 on first case to select"""
        self.visible_element_mb3_click(CasesPageLocators.ACTIVE_1ST_ROW)

    def click_run_test_option(self):
        self.visible_element_click(CasesPageLocators.RUN_TEST_OPT_LNK)

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

    def click_statistics_option(self):
        statistics = self.visible_element_click(CasesPageLocators.STATISTICS_BTN)
        return statistics

    def click_nth_case(self):
        """Click on nth case to select"""
        self.visible_element_click((By.CSS_SELECTOR, "tbody .clickable-row:nth-child(" + str(n) + ") .td:nth-child(2)"))

    def get_nth_case_id(self, n):
        """Get nth test case id"""
        id = self.visible_element_get_text((By.CSS_SELECTOR, "tbody .clickable-row:nth-child(" + str(n) + ") .tcid a"))
        return id

    def get_nth_case_name(self, n):
        """Get nth test case name"""
        name = self.visible_element_get_text(
            (By.CSS_SELECTOR, "tbody .clickable-row:nth-child(" + str(n) + ") td:nth-child(2) p"))
        return name

    def get_nth_case_tester_name(self, n):
        """Get nth test case tester name"""
        tester_name = self.visible_element_get_text(
            (By.CSS_SELECTOR, "tbody .clickable-row:nth-child(" + str(n) + ") .centered p"))
        return tester_name

    def get_nth_case_status(self, n):
        """Get nth test case status"""
        case_status = self.visible_element_get_text(
            (By.CSS_SELECTOR, "tbody .clickable-row:nth-child(" + str(n) + ") .testCaseState p"))
        return case_status
