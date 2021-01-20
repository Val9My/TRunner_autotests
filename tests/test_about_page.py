import time
from locators import locators
from pages.welcome_page import WelcomePage
from pages.suites_info_page import SuitesPage
from pages.about_page import AboutPage
import pytest
from utils.constants import LOGIN, PASSWORD

@pytest.mark.navbar
def test_navbar_is_visible(browser):
    "Test that navbar is visible"
    about_page = AboutPage(browser)
    about_page.load()
    time.sleep(1)
    assert about_page.is_element_seen(locators.AboutPageLocators.TRUNNER_LNK)

@pytest.mark.main
def test_about_us_title(browser):
    """Test that 'About' page title is seen"""
    about_page = AboutPage(browser)
    about_page.load()
    assert about_page.get_title() == locators.AboutPageLocators.ABOUT_TITLE

@pytest.mark.trunnercard
def test_trunner_card_is_visible(browser):
    "Test that trunner card is visible"
    about_page = AboutPage(browser)
    about_page.load()
    time.sleep(1)
    assert about_page.is_element_seen(locators.AboutPageLocators.TRUNNER_CARD)

@pytest.mark.about
def test_logout(browser):
    """Test that 'Sign In' page is seen if select 'Logout' option in 'Hello, User' dropdown"""
    welcome_page = WelcomePage(browser)
    about_page = AboutPage(browser)
    suites_info_page = SuitesPage(browser)
    welcome_page.load()
    welcome_page.input_text_in_username_tb_in(LOGIN)
    welcome_page.input_text_in_password_tb_in(PASSWORD)
    welcome_page.sign_in_btn_in_click()
    time.sleep(1)  # need timer to wait until suites page loading
    suites_info_page.about_btn_click()
    time.sleep(1)  # need timer to wait until about page loading
    about_page.get_title()
    about_page.hello_user_click()
    about_page.logout_click()
    assert about_page.get_title() == 'Sign In'

@pytest.mark.settings
def test_setting(browser):
    "Test that 'Settings' page is seen if select 'Settings' option in 'Hello, User' dropdown"
    welcome_page = WelcomePage(browser)
    about_page = AboutPage(browser)
    suites_info_page = SuitesPage(browser)
    welcome_page.load()
    welcome_page.input_text_in_username_tb_in(LOGIN)
    welcome_page.input_text_in_password_tb_in(PASSWORD)
    welcome_page.sign_in_btn_in_click()
    time.sleep(1)  # need timer to wait until suites page loading
    suites_info_page.about_btn_click()
    time.sleep(1)  # need timer to wait until about page loading
    about_page.hello_user_click()
    about_page.settings_click()
    assert browser.current_url == locators.SettingsPageLocators.SETTINGS_URL


@pytest.mark.trunner_lnk1
def test_trunner_link_logon_user(browser):
    "Test that Trunner_link is clickable and redirect user to the Suites(if user is logon)"
    about_page = AboutPage(browser)
    try:
        about_page.hello_user_click() #check if user is logon or not
    except:
        welcome_page = WelcomePage(browser)
        suites_info_page = SuitesPage(browser)
        welcome_page.load()
        welcome_page.input_text_in_username_tb_in(LOGIN)
        welcome_page.input_text_in_password_tb_in(PASSWORD)
        welcome_page.sign_in_btn_in_click()
        time.sleep(1)  # need timer to wait until suites page loading
    finally:
        browser.get(locators.AboutPageLocators.ABOUT_URL)
        time.sleep(1)  # need timer to wait until about page loading
        about_page.trunner_lnk_click()
        assert browser.current_url == locators.SuitesPageLocators.SUITES_URL

@pytest.mark.trunner_lnk2
def test_trunner_link_logout_user(browser):
    "Test that Trunner_link is clickable and redirect user to the welcome page (if user is logout)"
    about_page = AboutPage(browser)
    try:
        about_page.hello_user_click() #check if user logon
        about_page.logout_click() #user logout
    except:
        pass
    finally:
        browser.get(locators.AboutPageLocators.ABOUT_URL)
        time.sleep(1)
        about_page.trunner_lnk_click()
        assert browser.current_url == locators.WelcomePageLocators.WELCOME_URL


