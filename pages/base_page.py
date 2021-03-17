from utils.constants import DEFAULT_WAIT_TIME
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import BasePageLocators
import time
from selenium.webdriver.common.action_chains import ActionChains


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

    def visible_element_click(self, locator):
        """ Method to click on element when it get visible"""
        try:
            wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
            element = wait.until(EC.element_to_be_clickable(locator))
            # element = wait.until(EC.visibility_of_element_located(element))
            element.click()
        except TimeoutException:
            print(locator, f" not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print(locator, " in 'visible_element_click' - An Exception occurred:", e)

    def visible_element_mb3_click(self, locator):
        """ Method to click MB3 on element when it get visible"""
        try:
            chain = ActionChains(self.browser)
            wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
            element = wait.until(EC.element_to_be_clickable(locator))
            # element = wait.until(EC.visibility_of_element_located(element))
            chain.context_click(element).perform()
        except TimeoutException:
            print(locator, f" not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print(locator, " in 'visible_element_click' - An Exception occurred:", e)

    def visible_element_send_text(self, locator, text):
        """ Method to input text in element when it get visible"""
        try:
            wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
            wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
        except TimeoutException:
            print(locator, f" not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print(locator, " in 'visible_element_send_text' - An Exception occurred:", e)

    def visible_element_get_value(self, locator):
        """ Method to get text from element when it get visible"""
        try:
            wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
            element = wait.until(EC.visibility_of_element_located(locator))
            return element.text
            #return element.get_attribute('value')
        except TimeoutException:
            print(locator, f" not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print(locator, " in 'visible_element_get_value' - An Exception occurred:", e)

    def trunner_lnk_click(self):
        """ Click on 'TRunner' link"""
        self.visible_element_click(BasePageLocators.TRUNNER_LNK)

    def test_suites_lnk_click(self):
        """ Click on 'Test Suites' link """
        self.visible_element_click(BasePageLocators.TEST_SUITES_LNK)

    def suite_manager_lnk_click(self):
        """ Click on 'Suite Manager' link """
        self.visible_element_click(BasePageLocators.SUITE_MANAGER_LNK)

    def about_lnk_click(self):
        """ Click on 'About' link """
        self.visible_element_click(BasePageLocators.ABOUT_LNK)

    def hello_user_click(self):
        """ Click on 'Hello, User' drop-down """
        self.visible_element_click(BasePageLocators.HELLO_USER_DPDN)

    def user_settings_select(self):
        """ Click on 'Hello, User -> Settings' drop-down """
        self.visible_element_click(BasePageLocators.SETTINGS_OPT)

    def user_logout_select(self):
        """ Click on 'Hello, User -> Logout' drop-down """
        self.visible_element_click(BasePageLocators.LOGOUT_OPT)

    def get_user_name_from_hello(self):
        """ Get username in 'Hello, user' dropdown """
        try:
            wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
            user = wait.until(EC.visibility_of_element_located(BasePageLocators.HELLO_USER_DPDN)).text.partition(' ')[2]
            return user
        except TimeoutException:
            print(f" 'Hello, user' dropdown not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print(" In 'get_user_name_from_hello' - An Exception occurred:", e)

    def get_text_from_alert(self):
        """Getting text from alert dialog"""
        try:
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            return alert_text
        except TimeoutException:
            print(f" 'Alert' window not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print(" In 'get_text_from_alert' - An Exception occurred:", e)

    def handling_alert(self):
        """Alert acceptation"""
        try:
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert.accept()
        except TimeoutException:
            print(f" 'Alert' window not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print(" In 'handling_alert' - An Exception occurred:", e)

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





