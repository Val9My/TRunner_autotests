import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import WelcomePageLocators
from pages.base_page import BasePageElement
from utils.constants import DEFAULT_WAIT_TIME
import psycopg2
from utils.constants import *


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
        """Click on the 'SIGN IN' button on the Main Page"""
        try:
            self.visible_element_click(WelcomePageLocators.SIGN_IN_BTN_IN)
        except Exception as e:
            print("Error while click 'SIGN IN' button:", e)

    def sign_up_btn_in_click(self):
        """ Click on the 'SIGN UP' button on the Main Page"""
        try:
            self.visible_element_click(WelcomePageLocators.SIGN_UP_BTN_IN)
        except Exception as e:
            print("Error while click 'SIGN UP' button:", e)

    def sign_up_btn_up_click(self):
        """ Click on the 'SIGN UP' button on the Main Page"""
        try:
            self.visible_element_click(WelcomePageLocators.SIGN_UP_BTN_UP)
        except Exception as e:
            print("Error while click 'SIGN UP' button:", e)

    def about_us_btn_click(self):
        """Click 'ABOUT US' button on the Main Page"""
        try:
            self.visible_element_click(WelcomePageLocators.ABOUT_US_BTN)
        except Exception as e:
            print("Error while click 'ABOUT US' button:", e)

    def input_text_in_username_tb_in(self, text):
        """Input some text into 'Username' textbox on 'Sign In' page of main page"""
        try:
            self.visible_element_send_text(WelcomePageLocators.USER_NAME_TB_IN, text)
        except Exception as e:
            print("Error while input text into 'Username' textbox on Sign In page:", e)

    def input_text_in_password_tb_in(self, text):
        """Input some text into 'Password' textbox on 'Sign In' page of main page"""
        try:
            self.visible_element_send_text(WelcomePageLocators.PASSWORD_TB_IN, text)
        except Exception as e:
            print("Error while input text into 'Password' textbox on 'Sign In' page:", e)

    def input_text_in_username_tb_up(self, text):
        """Input some text into 'Username' textbox on 'Sign Up' page of main page"""
        try:
            self.visible_element_send_text(WelcomePageLocators.USER_NAME_TB_UP, text)
        except Exception as e:
            print("Error while input text into 'Username' textbox on 'Sign Up' page:", e)

    def input_text_in_password_tb_up(self, text):
        """Input some text into 'Password' textbox on 'Sign Up' page of main page"""
        try:
            self.visible_element_send_text(WelcomePageLocators.PASSWORD_TB_UP, text)
        except Exception as e:
            print("Error while input text into 'Password' textbox on 'Sign Up' page:", e)

    def input_text_in_invite_code_tb_up(self, text):
        """Input some text into 'Invite Code' textbox on 'Sign Up' page of main page"""
        try:
            self.visible_element_send_text(WelcomePageLocators.INVITE_TB_UP, text)
        except Exception as e:
            print("Error while input text into 'Invite Code' textbox on 'Sign Up' page:", e)

    def input_text_in_ado_token_tb_up(self, text):
        """Input some text into 'ADO token' textbox on 'Sign Up' page of main page"""
        try:
            self.visible_element_send_text(WelcomePageLocators.TOKEN_TB_UP, text)
        except Exception as e:
            print("Error while input text into 'ADO token' textbox on 'Sign Up' page:", e)











