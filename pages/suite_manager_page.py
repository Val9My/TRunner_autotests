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
        super().load(SuiteManagerPageLocators.SUITE_MANAGER_PAGE_LNK)

    def trunner_lnk_click(self):
        "Click on Trunner_lnk"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        trunner_lnk = wait.until(EC.visibility_of_element_located(locators.SuiteManagerPageLocators.TRUNNER_LNK))
        trunner_lnk.click()
