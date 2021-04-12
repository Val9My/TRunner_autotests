import pytest

from locators import locators
from locators.locators import SettingsPageLocators
from pages.settings_page import SettingsPage
from utils.constants import TEMP_TOKEN, DB_PASSWORD, TEMP_PASSW, PASSWORD, LOGIN


@pytest.mark.navbar
def test_username(browser, login, logout):
    """ Test that username is correct in 'Hello' dropdown """
    settings_page = SettingsPage(browser)
    settings_page.load()
    username = settings_page.get_user_name_from_hello()
    assert username == LOGIN

@pytest.mark.navigate
def test_trunner_link_logon_user(browser, login, close):
    """Test that Trunner_link is clickable and redirect user to the Suites(if user is logon)
    Test covers that user also is able to navigate backward"""
    settings_page = SettingsPage(browser)
    settings_page.load()
    settings_page.trunner_lnk_click()
    settings_page.backward()
    assert browser.current_url == locators.SettingsPageLocators.SETTINGS_URL


@pytest.mark.navigate
def test_add_suite_lnk(browser, login, close):
    """Test that Add_suite_lnk is clickable and redirecting user to the suites page if user login
    Test covers that user also is able to navigate backward"""
    settings_page = SettingsPage(browser)
    settings_page.load()
    settings_page.test_suites_lnk_click()
    settings_page.backward()
    assert browser.current_url == locators.SettingsPageLocators.SETTINGS_URL


@pytest.mark.navigate
def test_manage_suite_lnk(browser, login, close):
    """Test that Manage_suite_lnk is clickable and redirecting user to the suites manager page if user login
    Test covers that user also is able to navigate backward"""
    settings_page = SettingsPage(browser)
    settings_page.load()
    settings_page.suite_manager_lnk_click()
    settings_page.backward()
    assert browser.current_url == locators.SettingsPageLocators.SETTINGS_URL

@pytest.mark.token_input_test
def test_incorrect_token(browser,login,logout):
    """Test incorrect token input. Expected result: Error 'Check your input' highlighted is seen """
    settings_page = SettingsPage(browser)
    settings_page.load()
    settings_page.input_text_in_field(SettingsPageLocators.TOKEN_TB,TEMP_TOKEN)
    settings_page.update_token_btn_click()
    assert settings_page.is_element_seen(SettingsPageLocators.SAVE_FAILED) and \
           settings_page.visible_element_get_text(SettingsPageLocators.SAVE_FAILED)=="Check your input"

@pytest.mark.password_input_test
def test_mismatch_password(browser,login,logout):
    """Test mismatch in password input. Expected result: Alert 'Passwords are not the same. Please, check your input.' """
    settings_page = SettingsPage(browser)
    settings_page.load()
    settings_page.input_text_in_field(SettingsPageLocators.NEW_PASSWORD_TB, DB_PASSWORD)
    settings_page.input_text_in_field(SettingsPageLocators.CONFIRM_PASSWORD_TB, TEMP_PASSW)
    settings_page.update_password_btn_click()
    alert_text = settings_page.get_text_from_alert()  # get text from first alert
    settings_page.handling_alert()  # accept first allert
    assert alert_text=="Passwords are not the same. Please, check your input."


@pytest.mark.password_input_test
def test_password_match(browser,login,logout):
    """Test correct password input that match.
    Expected result: Changes are applied """
    settings_page = SettingsPage(browser)
    settings_page.load()
    settings_page.input_text_in_field(SettingsPageLocators.NEW_PASSWORD_TB, PASSWORD)
    settings_page.input_text_in_field(SettingsPageLocators.CONFIRM_PASSWORD_TB, PASSWORD)
    settings_page.update_password_btn_click()
    assert settings_page.is_element_seen(SettingsPageLocators.SAVE_SUCCESS) and \
           settings_page.visible_element_get_text(SettingsPageLocators.SAVE_SUCCESS)=="Saved"


@pytest.mark.title
def test_title_info(browser,login,logout):
    """Check that title is displayed and it is consistent"""
    settings_page = SettingsPage(browser)
    settings_page.load()
    text = settings_page.visible_element_get_text(SettingsPageLocators.SETTINGS_TITLE)
    assert text=="KYahorlytska's profile settings"