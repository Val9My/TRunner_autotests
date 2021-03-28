import pytest

from locators.locators import RunTestPageLocators
from pages.cases_page import CasesPage
from pages.run_test_page import RunTestPage
from pages.suites_info_page import SuitesPage


@pytest.mark.main1
def test_run_1st_case(browser, login, logout):
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.run_test_btn_click()
    run_test_page = RunTestPage(browser)
    run_test_page.wait_new_page_load()
    run_title = run_test_page.get_title()
    run_case_name = run_test_page.get_test_case_name()
    assert run_title == run_case_name, "Should be 'Run' page"
    run_test_page.back_to_suite_btn_click()



