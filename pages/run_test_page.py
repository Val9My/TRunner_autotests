import random

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import RunTestPageLocators
from pages.base_page import BasePageElement
from utils.constants import DEFAULT_WAIT_TIME
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class RunTestPage(BasePageElement):
    """
        Run page for running test cases (+ edit and create new bug options)
    """

    def __init__(self, browser):
        super().__init__(browser)

    def get_title(self):
        """Return title of the page"""
        title = self.browser.title
        # print(f"Run Test Page title = {str(title)}")
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
        self.visible_element_click(RunTestPageLocators.INFO_ICON)

    def info_icon_get_text(self):
        """Get text from 'I' info icon"""
        i_text = self.find_element(RunTestPageLocators.INFO_ICON).get_attribute('data-content')
        i_text = i_text.replace("<br />", "")
        i_text = i_text.replace("  ", "")
        i_text = i_text.replace("�️", "\n�")
        return i_text

    def info_tooltip_get_text(self):
        """Get text from popover 'I' icon tooltip"""
        popover_text = self.find_element(RunTestPageLocators.INFO_TOOLTIP).text
        return popover_text

    def info_icon_tooltip_is_visible(self):
        self.is_element_seen(RunTestPageLocators.INFO_TOOLTIP)

    def step_1_double_click(self):
        self.visible_element_double_click(RunTestPageLocators.TC_1ST_STEP_ROW)

    def case_status_dpdn_click(self):
        """Click on test case status dropdown on 'Run Test' page"""
        self.visible_element_click(RunTestPageLocators.TC_STATUS_DPDN)

    def get_case_status(self):
        """Get the 'Status' of test case"""
        select = Select(self.find_element(RunTestPageLocators.TC_STATUS_DPDN))
        selected_option = select.first_selected_option
        return selected_option.text

    def set_case_status(self, status):
        """Select the 'Status' of test case"""
        select = Select(self.find_element(RunTestPageLocators.TC_STATUS_DPDN))
        select.select_by_value(status)

    def get_test_case_name(self):
        """Get the test case title from 'Run Test' page"""
        name = self.visible_element_get_text(RunTestPageLocators.TC_TITLE)
        return name

    def is_saved_message_seen(self):
        """Check that 'SAVED' message popup"""
        if self.is_element_seen(RunTestPageLocators.SAVED_MESSAGE):
            return True
        else:
            print("'SAVED' message not pop up")
            return False

    def passed_btn_1_step_click(self):
        """Click on 'Passed' button for the 1st step on 'Run Test' page"""
        self.visible_element_click(RunTestPageLocators.TC_1ST_STEP_PASSED_BTN)

    def failed_btn_1_step_click(self):
        """Click on 'Failed' button for the 1st step on 'Run Test' page"""
        self.visible_element_click(RunTestPageLocators.TC_1ST_STEP_FAILED_BTN)

    def click_all_passed_btns(self):
        """Click 'Passed' buttons one by one"""
        self.click_several_buttons(RunTestPageLocators.TC_ALL_PASSED_BTNS)

    def click_all_failed_btns(self):
        """Click 'Failed' buttons one by one"""
        self.click_several_buttons(RunTestPageLocators.TC_ALL_FAILED_BTNS)

    def click_random_failed_btn(self):
        """Click random 'Failed' button"""
        try:
            wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
            buttons = wait.until(EC.presence_of_all_elements_located(RunTestPageLocators.TC_ALL_FAILED_BTNS))
            print("Buttons count= ", len(buttons))
            n = random.randint(0, len(buttons))
            buttons[n].click()
            print(f"Button {n} clicked")
        except TimeoutException:
            print(f"Buttons not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print("Buttons in 'click_random_failed_btn' - An Exception occurred:", e)

    def step_alt_click(self, locator):
        """ Method to start editing of test case step (ALT+MB1 click on step)"""
        try:
            chain = ActionChains(self.browser)
            element = self.find_element(locator)
            chain.key_down(Keys.ALT).click(element).key_up(Keys.ALT).perform()
        except Exception as e:
            print(f"Locator {locator} in 'visible_element_send_text' - An Exception occurred:", e)



