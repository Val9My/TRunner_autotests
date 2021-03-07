from utils.constants import DEFAULT_WAIT_TIME
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import BasePageLocators
import time


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        self.browser.get(url)

    def get_title(self):
        title = self.browser.title
        print(time.strftime("%Y-%m-%d | %H:%M:%S ") + "Page title = " + str(title))
        return title

    def visible_element_click(self, element):
        """ Method to click on element when it get visible"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        trunner_lnk = wait.until(EC.visibility_of_element_located(element))
        trunner_lnk.click()

    def visible_element_send_text(self, element, text):
        """ Method to input text in element when it get visible"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        wait.until(EC.visibility_of_element_located(element)).send_keys(text)

    def visible_element_get_value(self, element):
        """ Method to get text from element when it get visible"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        webelement = wait.until(EC.visibility_of_element_located(element))
        return webelement.get_attribute("value")

    def trunner_lnk_click(self):
        """ Click on 'TRunner' link"""
        try:
            self.visible_element_click(BasePageLocators.TRUNNER_LNK)
        except Exception as e:
            print("Error while click 'TRunner' button:", e)

    def test_suites_lnk_click(self):
        """ Click on 'Test Suites' link """
        try:
            self.visible_element_click(BasePageLocators.TEST_SUITES_LNK)
        except Exception as e:
            print("Error while click 'Test suites' button:", e)

    def suite_manager_lnk_click(self):
        """ Click on 'Suite Manager' link """
        try:
            self.visible_element_click(BasePageLocators.SUITE_MANAGER_LNK)
        except Exception as e:
            print("Error while click 'Suite Manager' button:", e)

    def about_lnk_click(self):
        """ Click on 'About' link """
        try:
            self.visible_element_click(BasePageLocators.ABOUT_LNK)
        except Exception as e:
            print("Error while click 'About' button:", e)

    def hello_user_click(self):
        """ Click on 'Hello, User' drop-down """
        try:
            self.visible_element_click(BasePageLocators.HELLO_USER_DPDN)
        except Exception as e:
            print("Error while click 'Hello, User' button:", e)

    def user_settings_select(self):
        """ Click on 'Hello, User -> Settings' drop-down """
        try:
            self.visible_element_click(BasePageLocators.SETTINGS_OPT)
        except Exception as e:
            print("Error while click 'Hello, User -> Settings' option:", e)

    def user_logout_select(self):
        """ Click on 'Hello, User -> Logout' drop-down """
        try:
            self.visible_element_click(BasePageLocators.LOGOUT_OPT)
        except Exception as e:
            print("Error while click 'Hello, User-> Logout' option:", e)



    def is_element_seen(self, locator):
        """ Check that element seen on page """
        try:
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException as e:
            print(locator, " - element is not seen timeout error", e)
            return False

    def wait_new_page_load(self):
        """ Check that current page URL changes to new """
        curr_url = self.browser.current_url  # get current URL
        try:
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.url_changes(curr_url))
        except Exception as e:
            print("error while waiting for loading new page:", e)
        finally:
            pass
        self.browser.get(self.browser.current_url)  # set new URL





