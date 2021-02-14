import time

from locators import locators
from pages.welcome_page import WelcomePage
from pages.suites_info_page import SuitesPage
import pytest

from utils.constants import LOGIN, PASSWORD


@pytest.mark.main
def test_workflow(browser, login, logout):
    """ Test that failed test cases numbers seen if click on FAILED 1st value """
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.failed_1_value_click()
    # time.sleep(1) #just to see action
    assert suites_page.is_element_seen(locators.SuitesPageLocators.FAILED_TC_1_1_LNK)


@pytest.mark.main1
def test_username(browser, login, logout):
    """ Test that username is correct in 'Hello' dropdown """
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    username = suites_page.get_user_name_from_hello()
    assert username == LOGIN
