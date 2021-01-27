import time

from locators import locators
from pages.base_page import BasePageElement
from pages.welcome_page import WelcomePage
from pages.suites_info_page import SuitesPage
from pages.about_page import AboutPage
import pytest

from utils.constants import LOGIN, PASSWORD, DEFAULT_WAIT_TIME


@pytest.mark.main
def test_signin_btn_seen_on_signup(browser):
    """Test that 'Sign In' button is seen on "SIGN UP" page """
    welcome_page = WelcomePage(browser)
    base_page = BasePageElement(browser)
    welcome_page.load()
    welcome_page.sign_up_btn_in_click()
    assert base_page.is_element_seen(locators.WelcomePageLocators.SIGN_IN_BTN_UP)


@pytest.mark.main
def test_username_tbox_hide(browser, logout):
    """Test that 'Username' textbox is NOT seen while click "SIGN UP" btn """
    welcome_page = WelcomePage(browser)
    base_page = BasePageElement(browser)
    welcome_page.load()
    welcome_page.sign_up_btn_in_click()
    assert not base_page.is_element_seen(locators.WelcomePageLocators.USER_NAME_TB_IN)


@pytest.mark.main
def test_about_us_page_is_open(browser):
    """Test that 'About' page title is seen after click 'About Us' btn """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.about_us_btn_click()
    assert welcome_page.get_title() == locators.AboutPageLocators.ABOUT_TITLE


@pytest.mark.main
def test_input_username_and_signin(browser):
    """Test that error is seen after input only 'Username' and Enter """
    welcome_page = WelcomePage(browser)
    base_page = BasePageElement(browser)
    welcome_page.load()
    welcome_page.input_text_in_username_tb_in('#%123')
    welcome_page.sign_in_btn_in_click()
    assert base_page.is_element_seen(locators.WelcomePageLocators.INVALID_CRED_ERROR)


@pytest.mark.main
def test_input_password_and_signin(browser):
    """Test that error is seen after input only 'Password' and Enter """
    welcome_page = WelcomePage(browser)
    base_page = BasePageElement(browser)
    welcome_page.load()
    welcome_page.input_text_in_password_tb_in('#%123')
    welcome_page.sign_in_btn_in_click()
    assert base_page.is_element_seen(locators.WelcomePageLocators.INVALID_CRED_ERROR)


@pytest.mark.main
def test_workflow(browser, logout):
    """Test smoke workflow"""
    welcome_page = WelcomePage(browser)
    suites_page = SuitesPage(browser)
    base_page = BasePageElement(browser)
    welcome_page.load()
    welcome_page.input_text_in_username_tb_in(LOGIN)
    welcome_page.input_text_in_password_tb_in(PASSWORD)
    welcome_page.sign_in_btn_in_click()
    base_page.wait_for_new_page_load()  # need timer to wait until suites page loading
    suites_page.failed_1_value_click()
    assert base_page.is_element_seen(locators.SuitesPageLocators.FAILED_TC_1_1_LNK)


@pytest.mark.main
def test_sign_in_click(browser, logout):
    """Test if click "SIGN IN" that 'Suites Info' page opens """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.input_text_in_username_tb_in(LOGIN)
    welcome_page.input_text_in_password_tb_in(PASSWORD)
    welcome_page.sign_in_btn_in_click()
    suites_page = SuitesPage(browser)
    assert suites_page.get_title() == 'Suites Info'


@pytest.mark.main
def test_sign2_in_click(browser, logout):
    """Test if click "SIGN IN" that 'Suites Info' page opens """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.input_text_in_username_tb_in(LOGIN)
    welcome_page.input_text_in_password_tb_in(PASSWORD)
    welcome_page.sign_in_btn_in_click()
    suites_info_page = SuitesPage(browser)
    assert suites_info_page.get_title() == 'Suites Info'