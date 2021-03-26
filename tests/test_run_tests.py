import pytest
import time
from locators.locators import RunTestPageLocators
from pages.base_page import BasePageElement
from locators.locators import SuitesPageLocators
from pages.cases_page import CasesPage
from pages.suites_info_page import SuitesPage
from pages.run_test_page import RunTestPage


def open_run_test_page_for_1st_test(browser):
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.run_test_btn_click()
    cases_page.wait_new_page_load()


@pytest.mark.smoke
@pytest.mark.main
def test_back_to_suite_click(browser, login, logout):
    """Test that 'Cases' page opened after 'Back to Suite' icon in 'Run' page"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    case_title = cases_page.get_title()
    cases_page.run_test_btn_click()
    cases_page.wait_new_page_load()
    run_test_page = RunTestPage(browser)
    run_test_page.back_to_suite_btn_click()
    run_test_page.wait_new_page_load()
    assert run_test_page.get_title() == case_title, "Should be 'Cases' page"


@pytest.mark.main
def test_info_icon_click(browser, login, logout):
    """Test that seen options for popups 'Info' icon options are the same as in 'Info' icon text """
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.info_icon_click()
    text = run_test_page.info_icon_get_text()
    tooltip_text = run_test_page.info_tooltip_get_text()
    assert text == tooltip_text

