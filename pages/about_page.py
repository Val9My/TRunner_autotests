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
        super().load(AboutPageLocators.ABOUT_URL)



