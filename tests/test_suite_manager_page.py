import time
from locators import locators
from pages.suite_manager_page import SuiteManagerPage
import pytest
from utils.constants import *


@pytest.mark.trunner_brand
def test_trunner_link(browser, login, logout):
    """Test that trunner brand is clickable and redirect user to suites in case user login """
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.trunner_lnk_click()
    assert browser.current_url == locators.SuitesPageLocators.SUITES_URL


@pytest.mark.test_suite_selector
def test_suite_selector_scenario1(browser, login, logout):
    """Check selecting third option Nadiia - Test Design from test suites
    Expected result: first test case id 49256, name Frameworks - Interpretation View"""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.suites_option_select_by_index(2)
    suites_manager_page.tc_checkbox_option_click(1)
    assert suites_manager_page.get_id_tc_value(1) == 49256\
           and suites_manager_page.get_tc_title(1) == 'Frameworks - Interpretation View'


@pytest.mark.test_suite_selector
def test_suite_selector_scenario2(browser, login, logout):
    """Check selecting fourth option Kulpat-Linux-20.6.5 from test suites
    Expected result: first test case id 49303, name Shortcut keys for Pseudo Wells Interpretation View in Map Editor."""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.suites_option_select_by_index(3)
    suites_manager_page.tc_checkbox_option_click(1)
    assert suites_manager_page.get_id_tc_value(1) == 49303\
           and suites_manager_page.get_tc_title(1) == 'Shortcut keys for Pseudo Wells Interpretation View in Map Editor.'

@pytest.mark.test_suite_selector
def test_suite_selector_scenario3(browser, login, logout):
    """Check selecting 6th option Kiran-Windows-20.6.4 from test suites
    Expected result: first test case id 49307, name Shortcut keys for Vertical Image Interpretation View in Section Editor."""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.suites_option_select_by_index(5)
    suites_manager_page.tc_checkbox_option_click(1)
    assert suites_manager_page.get_id_tc_value(1) == 49307 \
            and suites_manager_page.get_tc_title(1) == 'Shortcut keys for Vertical Image Interpretation View in Section Editor.'

@pytest.mark.add_test_case_modal_window
def test_suite_add_test_case_modal_window_scenario1(browser, login, logout):
    """Check that on clicking '+Add' opened new modal window 'Add to Test Suite' \n"
     "and user is able to select checkbox near test case and close modal window without adding new test cases"
     "Expected result: first test case id 50012, name Inventory: Inventory tree items restored with no active editor and Inventory view in docked and undocked state"""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.add_modal_window()
    suites_manager_page.click_checkbox_in_modal_add_window()
    suites_manager_page.close_add_test_modal_window()
    assert suites_manager_page.get_id_tc_value(1) == 50012\
           and suites_manager_page.get_tc_title(1) == "Inventory: Inventory tree items restored with no active editor and Inventory view in docked and undocked state"


@pytest.mark.handling_alert
def test_handling_alert_on_delete_scenario1(browser, login, logout):
    """Check that by clicking on '-Delete' appears 2 alerts
     Expected result: only managers allowed to delete test cases from suites"""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.click_delete_button()
    first_alert_text = suites_manager_page.get_text_from_alert()#get text from first alert
    suites_manager_page.handling_alert() #accept first allert
    second_alert_text = suites_manager_page.get_text_from_alert()#get text from the second alert
    suites_manager_page.handling_alert() #accept second alert
    assert first_alert_text == "Do you really want to delete following test cases from the suite?\n"\
           and second_alert_text == "Cannot delete the test case. Only managers allowed to remove test cases from suites."


@pytest.mark.search_for_test_case
def test_search_for_test_case_scenario1(browser, login, logout):
    """Checking search field.  From 'Nadiia - Test Design' entering in search field text 'inventory'"
    "Expected result: four test cases are found"""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.input_text_in_search_field(SEARCH_FOR_TEST_CASE1)
    cases = browser.find_elements(*locators.SuiteManagerPageLocators.FILTRATED_CASES)
    assert len(cases) == 4

@pytest.mark.search_for_test_case
def test_search_for_test_case_scenario2(browser, login, logout):
    """Checking search field.  From 'Kiran-Windows-20.6.4' entering in search field text 'short',then clear text."
    "Expected result: six test cases are found"""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.suites_option_select_by_index(5)
    suites_manager_page.input_text_in_search_field(SEARCH_FOR_TEST_CASE2)
    for i in range(len(SEARCH_FOR_TEST_CASE2)):
        suites_manager_page.backspace_in_search_field()
    cases = browser.find_elements(*locators.SuiteManagerPageLocators.FILTRATED_CASES)
    assert len(cases) == 6

@pytest.mark.search_for_test_case
def test_search_for_test_case_scenario3(browser, login, logout):
    """Checking search field.  From 'Kiran-Windows-20.6.4' entering in search field text 'short'."
    "Expected result: two test cases are found"""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.suites_option_select_by_index(5)
    suites_manager_page.input_text_in_search_field(SEARCH_FOR_TEST_CASE2)
    cases = browser.find_elements(*locators.SuiteManagerPageLocators.FILTRATED_CASES)
    assert len(cases) == 2

@pytest.mark.search_for_test_case
def test_search_for_test_case_parametrized(browser, login, logout, search_test_case):
    """Checking search field.  From 'Nadiia - Test Design' entering in search field different inappropriate text"
    "Expected result: no test cases are found"""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.input_text_in_search_field(search_test_case)
    cases = browser.find_elements(*locators.SuiteManagerPageLocators.FILTRATED_CASES)
    assert len(cases) == 0


@pytest.mark.test_create_suite_dropdown
def test_create_suite_from_ado(browser, login, logout):
    """Smoke test of create suite from ADO query on the suite manager page"""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.click_create_suite_button()
    suites_manager_page.create_from_ado_query()
    suites_manager_page.close_create_from_ado_query_window()

@pytest.mark.test_create_suite_dropdown
def test_create_suite_from_empty_suite(browser, login, logout):
    """Smoke test of create empty from create suite dropdown on the suite manager page"""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.click_create_suite_button()
    suites_manager_page.create_empty_suite()
    suites_manager_page.close_create_empty_suite_window()

@pytest.mark.test_create_suite_dropdown
def test_create_suite_from_existing_suite(browser, login, logout):
    """Smoke test of copy suite option from create suite dropdown on the suite manager page"""
    suites_manager_page = SuiteManagerPage(browser)
    suites_manager_page.load()
    suites_manager_page.click_create_suite_button()
    suites_manager_page.create_from_existing_suite()
    suites_manager_page.close_copy_test_suite_window()
