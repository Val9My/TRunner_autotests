import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import SettingsPageLocators
from utils.constants import DEFAULT_WAIT_TIME


class SuitesPage:
    """
        Settings page for updating ADO token and changing password
    """

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        title = wait.until(EC.visibility_of_element_located(SettingsPageLocators.SETTINGS_URL))
        self.browser.get(SettingsPageLocators.SETTINGS_URL)

    def get_title(self):
        title = self.browser.title
        print(time.strftime("%Y-%m-%d | %H:%M:%S ") + "Settings Page title = " + str(title))
        return title

