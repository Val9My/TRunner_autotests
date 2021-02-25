
from locators import locators
from pages.suite_manager_page import SuiteManagerPage
import pytest

from utils.constants import SEARCH_FOR_TEST_CASE


@pytest.mark.trunner_brand
def test_trunner_link(browser, login, logout):
    """Test that trunner brand is clickable and redirect user to suites in case user login """
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.trunner_lnk_click()
    assert browser.current_url == locators.SuitesPageLocators.SUITES_URL


@pytest.mark.test_suite_selector_scenario1
def test_suite_selector_selector_scenario1(browser, login,logout):
    """Check selecting third option Nadiia - Test Design from test suites
    Expected result: first test case id 49256, name Frameworks - Interpretation View"""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.suites_option_select_by_index(2)
    suites_manager_page.tc_checkbox_option_click(1)
    assert suites_manager_page.get_id_tc_value(1) == 49256\
           and suites_manager_page.get_tc_title(1)=='Frameworks - Interpretation View'


@pytest.mark.add_test_case_modal_window
def test_suite_add_test_case_modal_window_scenario1 (browser, login,logout):
    ("Check that on clicking '+Add' opened new modal window 'Add to Test Suite' \n"
     "and user is able to select checkbox near test case and close modal window without adding new test cases"
     "Expected result: first test case id 50012, name Inventory: Inventory tree items restored with no active editor and Inventory view in docked and undocked state")
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.add_modal_window()
    suites_manager_page.click_checkbox_in_modal_add_window()
    suites_manager_page.close_add_test_modal_window()
    assert suites_manager_page.get_id_tc_value(1)==50012\
           and suites_manager_page.get_tc_title(1)=="Inventory: Inventory tree items restored with no active editor and Inventory view in docked and undocked state"


@pytest.mark.handling_alert
def test_handling_alert_on_delete_scenario1 (browser, login,logout):
    ("Check that by clicking on '-Delete' appears 2 alerts"
     "Expected result: only managers allowed to delete test cases from suites")
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.click_delete_button()
    first_alert_text = suites_manager_page.get_text_from_alert()#get text from first alert
    suites_manager_page.handling_alert() #accept first allert
    second_alert_text = suites_manager_page.get_text_from_alert()#get text from the second alert
    suites_manager_page.handling_alert() #accept second alert
    assert first_alert_text == "Do you really want to delete following test cases from the suite?\n"\
           and second_alert_text=="Cannot delete the test case. Only managers allowed to remove test cases from suites."

@pytest.mark.search_for_test_case
def test_search_for_test_case(browser, login, logout):
    "Checking search field.  From 'Nadiia - Test Design' entering in search field text 'inventory'"
    "Expected result: four test cases are found"
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.input_text_in_search_field(SEARCH_FOR_TEST_CASE)
    cases=browser.find_elements(*locators.SuiteManagerPageLocators.FILTRATED_CASES)
    assert len(cases)==4

@pytest.mark.search_for_test_case
def test_search_for_test_case(browser, login, logout, SEARCH_FOR_TEST_CASE):
    "Checking search field.  From 'Nadiia - Test Design' entering in search field text 'inventory'"
    "Expected result: four test cases are found"
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.input_text_in_search_field(SEARCH_FOR_TEST_CASE)
    cases=browser.find_elements(*locators.SuiteManagerPageLocators.FILTRATED_CASES)
    assert len(cases)==4

@pytest.mark.search_for_test_case
def test_search_for_test_case_parametrized(browser, login, logout, search_test_case):
    "Checking search field.  From 'Nadiia - Test Design' entering in search field different inappropriate text"
    "Expected result: no test cases are found"
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.input_text_in_search_field(search_test_case)
    cases=browser.find_elements(*locators.SuiteManagerPageLocators.FILTRATED_CASES)
    assert len(cases)==0