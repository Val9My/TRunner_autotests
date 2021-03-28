import pytest
from locators.locators import SettingsPageLocators
from pages.settings_page import SettingsPage
from utils.constants import TEMP_TOKEN, DB_PASSWORD, TEMP_PASSW, PASSWORD


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
