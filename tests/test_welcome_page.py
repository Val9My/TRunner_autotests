import time

from locators import locators
from pages.welcome_page import WelcomePage
from pages.suites_info_page import SuitesPage
from pages.about_page import AboutPage
import pytest

from utils.constants import LOGIN, PASSWORD


@pytest.mark.main
def test_username_tbox_hide(browser):
    """Test that 'Username' textbox is not seen while click "SIGN UP" btn """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.sign_up_btn_in_click()
    welcome_page.is_element_seen(locators.WelcomePageLocators.SIGN_IN_BTN_UP)
    # time.sleep(3)  # need wait for sign up page loading, otherwise element is steel seen
    assert not welcome_page.is_element_seen(locators.WelcomePageLocators.USER_NAME_TB_IN)


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
    welcome_page.load()
    welcome_page.input_text_in_username_tb_in('#%123')
    welcome_page.sign_in_btn_in_click()
    assert welcome_page.is_element_seen(locators.WelcomePageLocators.INVALID_CRED_ERROR)


@pytest.mark.main
def test_input_password_and_signin(browser):
    """Test that error is seen after input only 'Password' and Enter """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.input_text_in_password_tb_in('#%123')
    welcome_page.sign_in_btn_in_click()
    assert welcome_page.is_element_seen(locators.WelcomePageLocators.INVALID_CRED_ERROR)


@pytest.mark.main1
def test_workflow(browser):
    """Test smoke workflow"""
    welcome_page = WelcomePage(browser)
    suites_page = SuitesPage(browser)
    welcome_page.load()
    welcome_page.input_text_in_username_tb_in(LOGIN)
    welcome_page.input_text_in_password_tb_in(PASSWORD)
    welcome_page.sign_in_btn_in_click()
    time.sleep(5)  # need timer to wait until suites page loading
    suites_page.failed_1_value_click()
    time.sleep(3)
    assert suites_page.is_element_seen(locators.SuitesPageLocators.FAILED_TC_1_1_LNK)


@pytest.mark.main1
def test_sign_in_click(browser):
    """Test if click "SIGN IN" that 'Suites Info' page opens """
    welcome_page = WelcomePage(browser)
    suites_page = SuitesPage(browser)
    about_page = AboutPage(browser)
    about_page.load()
    about_page.hello_user_click()
    about_page.logout_click()
    welcome_page.load()
    welcome_page.input_text_in_username_tb_in(LOGIN)
    welcome_page.input_text_in_password_tb_in(PASSWORD)
    welcome_page.sign_in_btn_in_click()
    assert suites_page.get_title() == 'Suites Info'



