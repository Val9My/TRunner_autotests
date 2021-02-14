from locators import locators
from pages.suite_manager_page import SuiteManagerPage
import pytest


@pytest.mark.trunner_brand
def test_trunner_link(browser, login, logout):
    """Test that trunner brand is clickable and redirect user to suites in case user login """
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.trunner_lnk_click()
    assert browser.current_url == locators.SuitesPageLocators.SUITES_URL


@pytest.mark.test_suite_selector_scenario1
def test_suite_selector_selector_scenario1(browser, login):
    '''Check selecting third option Nadiia - Test Design from test suites
    Expected result: first test case id 49256, name Frameworks - Interpretation View'''
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.suites_option_select_by_index(2)
    suites_manager_page.tc_checkbox_option_click(1)
    assert suites_manager_page.get_id_tc_value(1) == 49256 and suites_manager_page.get_tc_title(1)=='Frameworks - Interpretation View'
