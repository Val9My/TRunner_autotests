import pytest
from locators.locators import RunTestPageLocators
from pages.base_page import BasePageElement
from locators.locators import SuitesPageLocators
from pages.suites_info_page import SuitesPage
from pages.run_test_page import RunTestPage


@pytest.mark.main
def test_open_run_test_page_for_1st_test(browser, login, logout):
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.test_suites_lnk_click()


@pytest.mark.main
def test_run_1st_case(browser, login, logout):
    run_test_page = RunTestPage(browser)
    run_test_page.load("https://trunner.herokuapp.com/run/26/754")
    run_test_page.wait_new_page_load()
    run_test_page.get_test_case_name()
    title = run_test_page.get_test_case_name()
    status = run_test_page.get_test_status()


