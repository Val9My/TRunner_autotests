from utils.constants import DEFAULT_WAIT_TIME
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __init__(self, browser):
        self.browser = browser

    def load(self,url):
        self.browser.get(url)

    def is_element_seen(self, locator):
        """Check that element seen on page"""
        #self.browser.implicitly_wait(DEFAULT_WAIT_TIME) # need wait for page refresh (after sliding, action ...)
        try:
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException as e:
            print(locator, " - element is not seen timeout error", e)
            return False

    def wait_new_page_load(self):
        """Check that current page URL changes to new"""
        curr_url = self.browser.current_url  # get current URL
        try:
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.url_changes(curr_url))
        except Exception as e:
            print("error while waiting for loading new page from welcome page:", e)
        finally:
            pass
        self.browser.get(self.browser.current_url)  # set new URL




