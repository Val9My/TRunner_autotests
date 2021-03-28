import time
from locators.locators import SettingsPageLocators
from pages.base_page import BasePageElement


class SettingsPage(BasePageElement):
    """
        Settings page for updating ADO token and changing password
    """

    def __init__(self, browser):
        super().__init__(browser)

    def load(self):
        self.browser.get(SettingsPageLocators.SETTINGS_URL)

    def get_title(self):
        title = self.browser.title
        print(time.strftime("%Y-%m-%d | %H:%M:%S ") + "Settings Page title = " + str(title))
        return title

    def update_token_btn_click(self):
        """Click on 'Update token' button on 'Settings' page"""
        self.visible_element_click(SettingsPageLocators.UPDATE_TOKEN_BTN)

    def update_password_btn_click(self):
        """Click on 'Update password' button on 'Settings' page"""
        self.visible_element_click(SettingsPageLocators.UPDATE_PASSWORD_BTN)

    