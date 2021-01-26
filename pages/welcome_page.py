import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
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

    def input_text_in_password_tb_in(self, text):
        """Input some text into 'Password' textbox on Sign In page of main page"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        tbx = wait.until(EC.visibility_of_element_located(WelcomePageLocators.PASSWORD_TB_IN))
        tbx.send_keys(text)

    def input_text_in_username_tb_up(self, text):
        """Input some text into 'Username' textbox on 'Sign Up' page of main page"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        tbx = wait.until(EC.visibility_of_element_located(WelcomePageLocators.USER_NAME_TB_IN))
        tbx.send_keys(text)

    def input_text_in_password_tb_up(self, text):
        """Input some text into 'Password' textbox on 'Sign Up' page of main page"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        tbx = wait.until(EC.visibility_of_element_located(WelcomePageLocators.USER_NAME_TB_IN))
        tbx.send_keys(text)

    def input_text_in_invite_code_tb_up(self, text):
        """Input some text into 'Invite Code' textbox on 'Sign Up' page of main page"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        tbx = wait.until(EC.visibility_of_element_located(WelcomePageLocators.USER_NAME_TB_IN))
        tbx.send_keys(text)

    def input_text_in_ado_token_tb_up(self, text):
        """Input some text into 'ADO token' textbox on 'Sign Up' page of main page"""
        wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
        tbx = wait.until(EC.visibility_of_element_located(WelcomePageLocators.USER_NAME_TB_IN))
        tbx.send_keys(text)

    def wait_for_new_page_load(self):
        curr_url = WelcomePageLocators.WELCOME_URL
        try:
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.url_changes(curr_url))
        except Exception as e:
            print("error while waiting for loading new page from welcome page:", e)
        finally:
            pass
        self.browser.get(self.browser.current_url)







