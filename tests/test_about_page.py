from locators import locators
from pages.about_page import AboutPage
from pages.base_page import BasePageElement
import pytest

@pytest.mark.navbar
def test_navbar_is_visible(browser, logout, wait):
    "Test that navbar is visible"
    about_page = BasePageElement(browser)
    about_page.load()
    assert about_page.is_element_seen(locators.AboutPageLocators.TRUNNER_LNK)


@pytest.mark.main
def test_about_us_title(browser, logout):
    """Test that 'About' page title is seen"""
    about_page = AboutPage(browser)
    about_page.load()
    assert about_page.get_title() == locators.AboutPageLocators.ABOUT_TITLE


@pytest.mark.trunnercard
def test_trunner_card_is_visible(browser, logout):
    "Test that trunner card is visible"
    about_page = BasePageElement(browser)
    about_page.load()
    assert about_page.is_element_seen(locators.AboutPageLocators.TRUNNER_CARD)


@pytest.mark.about
def test_logout(browser, login, wait):
    """Test that 'Sign In' page is seen if select 'Logout' option in 'Hello, User' dropdown"""
    about_page = AboutPage(browser)
    about_page.load()
    about_page.hello_user_click()
    about_page.logout_click()
    assert about_page.get_title() == 'Sign In'


@pytest.mark.settings
def test_setting(browser,login, logout, wait):
    "Test that 'Settings' page is seen if select 'Settings' option in 'Hello, User' dropdown"
    about_page = AboutPage(browser)
    about_page.load()
    about_page.hello_user_click()
    about_page.settings_click()
    assert browser.current_url == locators.SettingsPageLocators.SETTINGS_URL


@pytest.mark.trunner_lnk2
def test_trunner_link_logon_user(browser,login, logout, wait):
    "Test that Trunner_link is clickable and redirect user to the Suites(if user is logon)"
    about_page = AboutPage(browser)
    about_page.load()
    about_page.trunner_lnk_click()
    assert browser.current_url == locators.SuitesPageLocators.SUITES_URL


@pytest.mark.trunner_lnk2
def test_trunner_link_logout_user(browser, wait):
    "Test that Trunner_link is clickable and redirect user to the welcome page (if user is logout)"
    about_page = AboutPage(browser)
    about_page.load()
    about_page.trunner_lnk_click()
    assert browser.current_url == locators.WelcomePageLocators.WELCOME_URL


@pytest.mark.add_suite_lnk
def test_add_suite_lnk(browser, login, logout, wait):
    "Test that Add_suite_lnk is clickable and redirecting user to the suites page if user login"
    about_page = AboutPage(browser)
    about_page.load()
    about_page.test_suites_lnk_click()
    assert browser.current_url == locators.SuitesPageLocators.SUITES_URL

@pytest.mark.add_suite_lnk
def test_manage_suite_lnk(browser, login, logout, wait):
    "Test that Manage_suite_lnk is clickable and redirecting user to the suites manager page if user login"
    about_page = AboutPage(browser)
    about_page.load()
    about_page.manage_suites_lnk_click()
    assert browser.current_url == locators.SuiteManagerPageLocators.SUITE_MANAGER_PAGE_LNK
