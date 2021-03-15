import time

from locators import locators
from pages.welcome_page import WelcomePage
from pages.suites_info_page import SuitesPage
from pages.about_page import AboutPage
import pytest
from utils.constants import *


@pytest.mark.main
def test_sign_in_btn_seen_on_signup(browser):
    """Test that 'Sign In' button is seen on "SIGN UP" page """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.wait_new_page_load()
    welcome_page.sign_up_btn_in_click()
    assert welcome_page.is_element_seen(locators.WelcomePageLocators.SIGN_IN_BTN_UP)


@pytest.mark.main
def test_username_tbox_hide(browser):
    """Test that 'Username' textbox is NOT seen while click "SIGN UP" btn """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.sign_up_btn_in_click()
    assert not welcome_page.is_element_seen(locators.WelcomePageLocators.USER_NAME_TB_IN)


@pytest.mark.main
def test_about_us_page_is_open(browser):
    """Test that 'About' page title is seen after click 'About Us' btn """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.about_us_btn_click()
    assert welcome_page.get_title() == locators.BasePageLocators.ABOUT_TITLE


@pytest.mark.main
def test_input_username_and_sign_in(browser, parametrized_username):
    """Test that error is seen after input only 'Username' and Enter """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.input_text_in_username_tb_in(parametrized_username)
    welcome_page.sign_in_btn_in_click()
    assert welcome_page.is_element_seen(locators.WelcomePageLocators.INVALID_CRED_ERROR)


@pytest.mark.main
def test_input_password_and_sign_in(browser, parametrized_password):
    """Test that error is seen after input only 'Password' and Enter """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.input_text_in_password_tb_in(parametrized_password)
    welcome_page.sign_in_btn_in_click()
    assert welcome_page.is_element_seen(locators.WelcomePageLocators.INVALID_CRED_ERROR)


@pytest.mark.main
def test_input_login_password_and_sign_in(browser, parametrized_username, parametrized_password):
    """Test that error is seen after input invalid "Username' and 'Password' and Enter """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.input_text_in_username_tb_in(parametrized_username)
    welcome_page.input_text_in_password_tb_in(parametrized_password)
    welcome_page.sign_in_btn_in_click()
    time.sleep(1)
    assert welcome_page.is_element_seen(locators.WelcomePageLocators.INVALID_CRED_ERROR)


@pytest.mark.main
def test_smoke_workflow(browser, login, logout):
    """Test smoke workflow"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()  # need timer to wait until suites page loading
    suites_page.failed_1_value_click()
    assert suites_page.is_element_seen(locators.SuitesPageLocators.FAILED_TC_1_1_LNK), "No filed test cases in 1st row"


@pytest.mark.main
def test_sign_in_click_with_login_fixture(browser, login, logout):
    """Test if click "SIGN IN" that 'Suites Info' page opens """
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    assert suites_page.get_title() == 'Suites Info', "Should open Test Suites page"


@pytest.mark.main
def test_trunner_card_seen_in_sign_up(browser):
    """Test 'TRunner' logo and link seen on 'Sign Up' page """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.sign_up_btn_in_click()
    assert welcome_page.is_element_seen(locators.WelcomePageLocators.TRUNNER_UP_LNK), \
        "Should be seen 'TRunner logo and link'"


@pytest.mark.main
def test_alert_sign_up_click_with_username(browser, parametrized_username, close):
    """Test click 'Sign Up' button with only Username input in 'Sign Up' page"""
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.sign_up_btn_in_click()
    welcome_page.input_text_in_username_tb_up(parametrized_username)
    welcome_page.sign_up_btn_up_click()
    alert_text = welcome_page.get_text_from_alert()
    welcome_page.handling_alert()
    assert alert_text == 'Invalid Invite Code. Please, double check it and try again.',\
        "Should pops up alert window"


@pytest.mark.main
def test_alert_sign_up_click_with_username_and_ado_token(browser, parametrized_username, close):
    """Test click 'Sign Up' button with 'Username' and 'ADO Token' input in 'Sign Up' page"""
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.sign_up_btn_in_click()
    welcome_page.input_text_in_username_tb_up(parametrized_username)
    welcome_page.input_text_in_ado_token_tb_up(parametrized_username)
    welcome_page.sign_up_btn_up_click()
    alert_text = welcome_page.get_text_from_alert()
    welcome_page.handling_alert()
    assert alert_text == 'Invalid Invite Code. Please, double check it and try again.', "Should pops up alert window"


@pytest.mark.main
def test_alert_sign_up_click_with_username_and_ado_token_and_invite_code(browser, parametrized_username, close):
    """Test click 'Sign Up' button with 'Username' and 'ADO Token' and 'Invite Code' input in 'Sign Up' page"""
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.sign_up_btn_in_click()
    welcome_page.input_text_in_username_tb_up(parametrized_username)
    welcome_page.input_text_in_ado_token_tb_up(parametrized_username)
    welcome_page.input_text_in_invite_code_tb_up(parametrized_username)
    welcome_page.sign_up_btn_up_click()
    alert_text = welcome_page.get_text_from_alert()
    welcome_page.handling_alert()
    assert alert_text == 'Invalid Invite Code. Please, double check it and try again.', "Should pops up alert window"


@pytest.mark.main
def test_alert_sign_up_click_with_username__ado_token__invite_code__password(browser, parametrized_username, close):
    """Test click 'Sign Up' button with 'Username' and 'ADO Token' and 'Invite Code' and 'Password' in 'Sign Up' page"""
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.sign_up_btn_in_click()
    welcome_page.input_text_in_username_tb_up(parametrized_username)
    welcome_page.input_text_in_ado_token_tb_up(parametrized_username)
    welcome_page.input_text_in_invite_code_tb_up(parametrized_username)
    welcome_page.input_text_in_password_tb_up(TEMP_PASSW)
    welcome_page.sign_up_btn_up_click()
    alert_text = welcome_page.get_text_from_alert()
    welcome_page.handling_alert()
    assert alert_text == 'Invalid Invite Code. Please, double check it and try again.', "Should pops up alert window"


@pytest.mark.main
@pytest.mark.temp_user
def test_sign_up_workflow_for_new_user(browser, delete_temp_user):
    """Test 'Sign Up' workflow for new user (Temp User) """
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.sign_up_btn_in_click()
    welcome_page.input_text_in_username_tb_up(TEMP_USER)
    welcome_page.input_text_in_ado_token_tb_up(TEMP_TOKEN)
    welcome_page.input_text_in_invite_code_tb_up(INV_CODE)
    welcome_page.input_text_in_password_tb_up(TEMP_PASSW)
    welcome_page.sign_up_btn_up_click()
    welcome_page.input_text_in_username_tb_in(TEMP_USER)
    welcome_page.input_text_in_password_tb_in(TEMP_PASSW)
    welcome_page.sign_in_btn_in_click()
    assert welcome_page.get_user_name_from_hello() == 'TempUser', "Should be temp user 'TempUser'"


