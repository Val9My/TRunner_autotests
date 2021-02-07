import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import AboutPageLocators
from locators.locators import SuiteManagerPageLocators
from pages.base_page import BasePageElement
from utils.constants import DEFAULT_WAIT_TIME


class AboutPage(BasePageElement):
    """
        About page
    """

    def __init__(self, browser):
        super().__init__(browser)

    def load(self):
        self.browser.get(AboutPageLocators.ABOUT_URL)

    def get_title(self):
        title = self.browser.title
        print(time.strftime("%Y-%m-%d | %H:%M:%S ") + "Main Page title = " + str(title))
        return title

    def hello_user_click(self):
        """Click on 'Hello, User' drop-down"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        hello_dpdn = wait.until(EC.visibility_of_element_located(AboutPageLocators.HELLO_USER_DPDN))
        hello_dpdn.click()

    def logout_click(self):
        """Click on 'Logout' option in 'Hello, User' context menu"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        logout = wait.until(EC.visibility_of_element_located(AboutPageLocators.LOGOUT_OPT))
        logout.click()

    def settings_click(self):
        "Click on 'Settings' option in 'Hello, User' context menu"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        settings = wait.until(EC.visibility_of_element_located(AboutPageLocators.SETTINGS_OPT))
        settings.click()

    def trunner_lnk_click(self):
        "Click on Trunner_lnk"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        trunner_lnk = wait.until(EC.visibility_of_element_located(AboutPageLocators.TRUNNER_LNK))
        trunner_lnk.click()

    def test_suites_lnk_click(self):
        "Click on test_suites button from about page"
        wait= WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        suites_lnk= wait.until(EC.visibility_of_element_located(AboutPageLocators.ADD_SUITE_LNK))
        suites_lnk.click()

    def manage_suites_lnk_click(self):
        "Click on Suites Manager button from about page"
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        manage_suits_lnk = wait.until(EC.visibility_of_element_located(SuiteManagerPageLocators.SUITE_MANAGER_LNK))
        manage_suits_lnk.click()


