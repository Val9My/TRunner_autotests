from locators import locators
from pages.about_page import AboutPage
from pages.base_page import BasePageElement
import pytest

@pytest.mark.navbar
def test_navbar_is_visible(browser, logout):
    "Test that navbar is visible"
    about_page = BasePageElement(browser)
    about_page.load(locators.AboutPageLocators.ABOUT_URL)
    assert about_page.is_element_seen(locators.AboutPageLocators.TRUNNER_LNK)

@pytest.mark.main
def test_about_us_title(browser, logout):
    """Test that 'About' page title is seen"""
    about_page = AboutPage(browser)
    about_page.load(locators.AboutPageLocators.ABOUT_URL)
    assert about_page.get_title() == locators.AboutPageLocators.ABOUT_TITLE


@pytest.mark.trunnercard
def test_trunner_card_is_visible(browser, logout):
    "Test that trunner card is visible"
    about_page = BasePageElement(browser)
    about_page.load(locators.AboutPageLocators.ABOUT_URL)
    assert about_page.is_element_seen(locators.AboutPageLocators.TRUNNER_CARD)


@pytest.mark.about
def test_logout(browser, login):
    """Test that 'Sign In' page is seen if select 'Logout' option in 'Hello, User' dropdown"""
    about_page = AboutPage(browser)
    about_page.load(locators.AboutPageLocators.ABOUT_URL)
    about_page.hello_user_click()
    about_page.logout_click()
    assert about_page.get_title() == 'Sign In'


@pytest.mark.settings
def test_setting(browser,login, logout):
    "Test that 'Settings' page is seen if select 'Settings' option in 'Hello, User' dropdown"
    about_page = AboutPage(browser)
    about_page.load(locators.AboutPageLocators.ABOUT_URL)
    about_page.hello_user_click()
    about_page.settings_click()
    assert browser.current_url == locators.SettingsPageLocators.SETTINGS_URL


@pytest.mark.trunner_lnk2
def test_trunner_link_logon_user(browser,login, logout):
    "Test that Trunner_link is clickable and redirect user to the Suites(if user is logon)"
    about_page = AboutPage(browser)
    about_page.load(locators.AboutPageLocators.ABOUT_URL)
    about_page.trunner_lnk_click()
    assert browser.current_url == locators.SuitesPageLocators.SUITES_URL


@pytest.mark.trunner_lnk2
def test_trunner_link_logout_user(browser):
    "Test that Trunner_link is clickable and redirect user to the welcome page (if user is logout)"
    about_page = AboutPage(browser)
    about_page.load(locators.AboutPageLocators.ABOUT_URL)
    about_page.trunner_lnk_click()
    assert browser.current_url == locators.WelcomePageLocators.WELCOME_URL


@pytest.mark.add_suite_lnk
def test_add_suite_lnk(browser, login, logout):
    "Test that Add_suite_lnk is clickable and redirecting user to the suites page if user login"
    about_page = AboutPage(browser)
    about_page.load(locators.AboutPageLocators.ABOUT_URL)
    about_page.test_suites_lnk_click()
    assert browser.current_url == locators.SuitesPageLocators.SUITES_URL

@pytest.mark.manage_suite_lnk
def test_manage_suite_lnk(browser, login, logout):
    "Test that Manage_suite_lnk is clickable and redirecting user to the suites manager page if user login"
    about_page = AboutPage(browser)
    about_page.load(locators.AboutPageLocators.ABOUT_URL)
    about_page.manage_suites_lnk_click()
    assert browser.current_url == locators.SuiteManagerPageLocators.SUITE_MANAGER_PAGE_LNK

@pytest.mark.text_card
def test_card_text(browser,logout):
    "Check the text on the About page"
    about_page = AboutPage(browser)
    about_page.load(locators.AboutPageLocators.ABOUT_URL)
    card_element=browser.find_element_by_xpath("//p[@class='lead']")
    assert card_element.text=="An Open Source solution to run test cases independently using Azure DevOps systems."

@pytest.mark.dropdown_options
def test_dropdown_options(browser,login,logout):
    "Check the available dropdown settings from the About page"
    about_page = AboutPage(browser)
    about_page.load(locators.AboutPageLocators.ABOUT_URL)
    about_page.hello_user_click()
    dropdown_elements_names = [x.text for x in browser.find_elements_by_xpath("//a[@class='dropdown-item']")]
    assert dropdown_elements_names[0][-8:]=='Settings' and dropdown_elements[1][-6:]=='Logout'

@pytest.mark.navbar_items_text_size

def test_navbar_items_size(browser,login,logout):
    "Check that the font-sizes of Test Suite,Suite Manager and About navbar items on the About Page are equal "
    about_page = AboutPage(browser)
    about_page.load(locators.AboutPageLocators.ABOUT_URL)
    navbar_elements_font_size=[x.value_of_css_property('font-size') for x in browser.find_elements_by_xpath("//li[@class='nav-item active']")]
    assert all(i == navbar_elements_font_size[0] for i in navbar_elements_font_size)