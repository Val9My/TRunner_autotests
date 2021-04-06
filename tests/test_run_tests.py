import pytest
import time
from locators.locators import RunTestPageLocators
from pages.base_page import BasePageElement
from locators.locators import SuitesPageLocators
from pages.cases_page import CasesPage
from pages.suites_info_page import SuitesPage
from pages.run_test_page import RunTestPage


def open_run_test_page_for_1st_test(browser):
    """Function to load 'Run' page for 1st test case"""
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
def test_save_and_close_icon_click(browser, login, logout):
    """Test that 'Cases' page opened after 'Save and Close' icon in 'Run' page"""
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
    run_test_page.failed_btn_1_step_click()
    run_test_page.passed_btn_1_step_click()
    run_test_page.save_and_close_btn_click()
    run_test_page.wait_new_page_load()
    test_page_title = run_test_page.get_title()
    assert test_page_title == case_title, "Should be 'Cases' page"


@pytest.mark.main
def test_username_for_1st_case_after_save_and_close_icon_click(browser, login, logout):
    """Test that 'Tester' name in 'Case' page is correct after 'Save and Close' in 'Run' page"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.failed_btn_1_step_click()
    run_test_page.passed_btn_1_step_click()
    run_test_page.save_and_close_btn_click()
    run_test_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    tester_name = cases_page.get_first_case_tester_name()
    user_name = cases_page.get_user_name_from_hello()
    assert tester_name == user_name, "Should be user name"


@pytest.mark.main
def test_trunner_click_in_run_page(browser, login, logout):
    """Test after 'TRunner' button click in 'Run' page - 'Suites' page opened"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.trunner_lnk_click()
    run_test_page.handling_alert()
    run_test_page.wait_new_page_load()
    suites_page = SuitesPage(browser)
    page_title = suites_page.get_title()
    assert page_title == 'Suites Info', "Should be 'Suites Info' for suites page'"


@pytest.mark.main
def test_report_bug(browser, login, close):
    """Test after 'Report a bug' button click in 'Run' page - 'ADO' page opened"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_title = run_test_page.get_title()
    run_test_page.report_a_bug_btn_click()
    run_test_page.wait_new_page_load()
    page_title = run_test_page.get_title()
    assert page_title == 'Sign in to your account' or 'ADO', "Should not be 'Cases' page'"


@pytest.mark.main
def test_info_icon_click(browser, login, logout):
    """Test that seen options for popups 'Info' icon options are the same as in 'Info' icon text """
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.info_icon_click()
    text = run_test_page.info_icon_get_text()
    tooltip_text = run_test_page.info_tooltip_get_text()
    assert text == tooltip_text
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_comment_seen_after_double_click_on_1st_step(browser, login, logout):
    """Test that Comment block is seen after double-click on 1st step row """
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.step_1_double_click()
    assert run_test_page.is_element_seen(RunTestPageLocators.TC_1ST_STEP_COMMENT_TB), "Comment should be seen"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_check_opened_test_case_status(browser, login, logout):
    """Check test case status in dropdown"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    #run_test_page.load("https://trunner.herokuapp.com/run/26/754")
    status = run_test_page.get_case_status()
    assert status == '💬', "Status should be none for opened test case"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_check_saved_message_seen_after_save_btn_click(browser, login, logout):
    """Check that 'Saved' message seen after 'Save' button clicked"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.failed_btn_1_step_click()
    run_test_page.passed_btn_1_step_click()
    run_test_page.save_btn_click()
    saved_message_popup = run_test_page.is_saved_message_seen()
    assert saved_message_popup, " Should 'SAVED' message popup"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.todo
def test_failed_case_status_seen_if_fail_step(browser, login, logout):
    """Check that 'Failed' test case status seen after 'Fail' button clicked for 1st step"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.failed_btn_1_step_click()
    run_test_page.save_btn_click()
    time.sleep(5)
    status = run_test_page.get_case_status()
    assert status == '❌', "Status should be 'Failed' for test case"
    run_test_page.back_to_suite_btn_click()





