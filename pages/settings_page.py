import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import SettingsPageLocators
from pages.base_page import BasePageElement
from utils.constants import DEFAULT_WAIT_TIME


class SettingsPage(BasePageElement):
    """
        Settings page for updating ADO token and changing password
    """

    def __init__(self, browser):
        super().__init__(browser)

    def load(self):
        self.browser.get(SettingsPageLocators.SETTINGS_URL)

    def get_title(self):
        title = self.browser.title
        print(time.strftime("%Y-%m-%d | %H:%M:%S ") + "Settings Page title = " + str(title))
        return title

