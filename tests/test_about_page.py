import time

from locators import locators
from pages.welcome_page import WelcomePage
from pages.suites_info_page import SuitesPage
from pages.about_page import AboutPage
import pytest
from utils.constants import LOGIN, PASSWORD


@pytest.mark.about
def test_logout(browser):
    """Test that 'Welcome page' is seen if select 'Logout' option in 'Hello, User' dropdown"""
    welcome_page = WelcomePage(browser)
    about_page = AboutPage(browser)
    suites_info_page = SuitesPage(browser)
    about_page.load()
    welcome_page.input_text_in_username_tb_in(LOGIN)
    welcome_page.input_text_in_password_tb_in(PASSWORD)
    welcome_page.sign_in_btn_in_click()
    time.sleep(1)  # need timer to wait until suites page loading
    suites_info_page.get_title()
    suites_info_page.failed_1_value_click()
    time.sleep(1) #just to see action
    assert suites_info_page.is_element_seen(locators.SuitesPageLocators.FAILED_TC_1_1_LNK)