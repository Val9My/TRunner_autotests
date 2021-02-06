import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import WelcomePageLocators
from pages.base_page import BasePageElement
from utils.constants import DEFAULT_WAIT_TIME


class WelcomePage(BasePageElement):
    """
        Main page for Sig In and Sign Up
    """

    def __init__(self, browser):
        super().__init__(browser)

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
        about_us_button = wait.until(EC.visibility_of_element_located(WelcomePageLocators.ABOUT_US_BTN))
        about_us_button.click()

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







