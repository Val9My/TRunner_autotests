import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import WelcomePageLocators
from utils.constants import DEFAULT_WAIT_TIME


class WelcomePage:
    """
        Main page for Sig In and Sign Up
    """

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        #wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        #title = wait.until(EC.visibility_of_element_located(WelcomePageLocators.WELCOME_URL))
        self.browser.get(WelcomePageLocators.WELCOME_URL)

    def get_title(self):
        title = self.browser.title
        print(time.strftime("%Y-%m-%d | %H:%M:%S ") + "Main Page title = " + str(title))
        return title

    def sign_in_btn_in_click(self):
        """Click on the "SIGN IN" button on the Main Page"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        sign_up_button = wait.until(EC.visibility_of_element_located(WelcomePageLocators.SIGN_IN_BTN_IN))
        sign_up_button.click()

    def sign_up_btn_in_click(self):
        """ Click on the "SIGN UP" button on the Main Page"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        sign_up_button = wait.until(EC.visibility_of_element_located(WelcomePageLocators.SIGN_UP_BTN_IN))
        sign_up_button.click()

    def about_us_btn_click(self):
        """Click on the "ABOUT US" button on the Main Page"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        sign_up_button = wait.until(EC.visibility_of_element_located(WelcomePageLocators.ABOUT_US_BTN))
        sign_up_button.click()

    def is_element_seen(self, locator):
        """Check that element seen on page"""
        try:
            element = WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException as e:
            print(locator, " - element is not seen timeout error", e)
            return False

    def input_text_in_username_tb_in(self, text):
        """Input some text into 'Username' textbox on Sign In page of main page"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        tbx = wait.until(EC.visibility_of_element_located(WelcomePageLocators.USER_NAME_TB_IN))
        tbx.send_keys(text)
        #tbx.send_keys(Keys.ENTER)

    def input_text_in_password_tb_in(self, text):
        """Input some text into 'Password' textbox on Sign In page of main page"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        tbx = wait.until(EC.visibility_of_element_located(WelcomePageLocators.PASSWORD_TB_IN))
        tbx.send_keys(text)
        #tbx.send_keys(Keys.ENTER)




