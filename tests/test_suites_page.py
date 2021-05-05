import time
from locators import locators
from pages.welcome_page import WelcomePage
from pages.suites_info_page import SuitesPage
from locators.locators import SuitesPageLocators
import pytest
from utils.constants import LOGIN, PASSWORD


@pytest.mark.main
def test_workflow(browser, login, logout):
    """ Test that failed test cases numbers seen if click on FAILED 1st value """
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.failed_1_value_click()
    # time.sleep(1) #just to see action
    assert suites_page.are_elements_seen(SuitesPageLocators.FAILED_HIDDEN_N_LNK)


@pytest.mark.main
def test_username(browser, login, logout):
    """ Test that username is correct in 'Hello' dropdown """
    suites_page = SuitesPage(browser)
    username = suites_page.get_user_name_from_hello()
    assert username == LOGIN


@pytest.mark.main
def test_cases_value_as_sum_of_test_cases_1st_row(browser, login, logout):
    """Test that "Test Cases" value is equal to sum of test cases in 1st row suite
        TEST_CASES_VALUE = PASSED_1_DPDN + FAILED_1_DPDN + BLOCKED_1_DPDN + NOT_EXECUTED_1_VALUE"""
    suites_page = SuitesPage(browser)
    t_c_value = int(suites_page.visible_nth_element_get_text(SuitesPageLocators.TEST_CASES_N_VALUE, 0))
    sum_value = suites_page.calculate_test_cases_value_as_sum_of_test_cases()
    assert t_c_value == sum_value, "'Test Case' value in 1st row suite"


@pytest.mark.main
def test_1st_row_suite_mb3_click(browser, login, logout):
    """Click MB3 on 1st row suite to see context menu"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.visible_nth_element_mb3_click(SuitesPageLocators.N_ROW, 0)
    assert suites_page.is_element_seen(SuitesPageLocators.SUITE_REPORT_OPT)
