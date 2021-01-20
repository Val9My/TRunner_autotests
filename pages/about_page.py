import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import AboutPageLocators
from utils.constants import DEFAULT_WAIT_TIME


class AboutPage:
    """
        About page
    """

    def __init__(self, browser):
        self.browser = browser

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

    def is_element_seen(self, locator):
        """Check that element seen on page"""
        try:
            element = WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException as e:
            print(locator, " - element is not seen timeout error", e)
            return False


    def logout_click(self):
        """Click on 'Logout' option in 'Hello, User' context menu"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        logout = wait.until(EC.visibility_of_element_located(AboutPageLocators.LOGOUT_OPT))
        logout.click()



