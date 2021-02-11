from locators import locators
from pages.suite_manager_page import SuiteManagerPage
import pytest

@pytest.mark.first
def test_trunner_link(browser, login, logout):
    """Test that trunner brand is clickable and redirect user to suites in case user login """
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.trunner_lnk_click()
    assert browser.current_url == locators.SuitesPageLocators.SUITES_URL