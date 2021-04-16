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


@pytest.mark.main
def test_case_name(browser, login, logout):
    """Test that test case name the same as opened in 'Cases' page"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    case_title = cases_page.get_first_case_name()
    cases_page.click_first_case()
    cases_page.click_mb3_first_case()
    cases_page.click_run_test_option()
    cases_page.wait_new_page_load()
    run_test_page = RunTestPage(browser)
    case_name = run_test_page.get_test_case_name()
    assert case_name == case_title, "Should be test case name"


@pytest.mark.smoke
@pytest.mark.main
def test_back_to_suite_click(browser, login, logout):
    """Test that 'Cases' page opened after 'Back to Suite' icon in 'Run' page"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    case_title = cases_page.get_title()
    cases_page.click_first_case()
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
    #run_title = run_test_page.get_title()
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
def test_add_comment_saved(browser, login, logout):
    """Test that comment added in Comment block and seen after reopen """
    tc_1st_comment_locator = RunTestPageLocators.TC_1ST_STEP_COMMENT_TB
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.step_1_double_click()
    comment_text = run_test_page.visible_element_get_text(tc_1st_comment_locator)
    run_test_page.visible_element_send_text(tc_1st_comment_locator, " New Added Comment")
    run_test_page.failed_btn_1_step_click()
    run_test_page.passed_btn_1_step_click()
    run_test_page.save_and_close_btn_click()
    run_test_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.wait_new_page_load()
    cases_page.click_first_case()
    cases_page.click_mb3_first_case()
    cases_page.click_run_test_option()
    run_test_page.step_1_double_click()
    new_comment_text = run_test_page.visible_element_get_text(tc_1st_comment_locator)
    assert new_comment_text == comment_text + ' New Added Comment', "Comment text should be seen in the end"
    run_test_page.visible_element_clear_text(tc_1st_comment_locator) # clear added text
    run_test_page.visible_element_send_text(tc_1st_comment_locator, comment_text)
    run_test_page.failed_btn_1_step_click()
    run_test_page.passed_btn_1_step_click()
    run_test_page.save_and_close_btn_click()
    cases_page.wait_new_page_load()


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


@pytest.mark.main
def test_click_passed_btn_is_active_for_1st_step(browser, login, logout):
    """Check that 'Passed' button is active and focus after click"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.passed_btn_1_step_click()
    assert 'focus active' in run_test_page.visible_element_get_class(RunTestPageLocators.TC_1ST_STEP_PASSED_BTN), \
        " 'focus active' should be in class"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_click_passed_btn_is_active_for_1st_step_after_save(browser, login, logout):
    """Check that 'Passed' button is active after click and save"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.passed_btn_1_step_click()
    run_test_page.save_btn_click()
    passed_class = run_test_page.visible_element_get_class(RunTestPageLocators.TC_1ST_STEP_PASSED_BTN)
    status = run_test_page.get_case_status()
    assert 'active' in passed_class and 'focus' not in passed_class\
        and status == '✅  Passed', \
        " only 'active' should be in class"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_click_failed_btn_is_active_for_1st_step(browser, login, logout):
    """Check that 'Failed' button is active and focus after click"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.failed_btn_1_step_click()
    failed_class = run_test_page.visible_element_get_class(RunTestPageLocators.TC_1ST_STEP_FAILED_BTN)
    assert 'focus active' in failed_class, " 'focus active' should be in class"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_case_status_failed_if_click_fail_step_and_save(browser, login, logout):
    """Check that 'Failed' test case status seen after 'Fail' button clicked for 1st step"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.failed_btn_1_step_click()
    run_test_page.save_btn_click()
    status = run_test_page.get_case_status()
    failed_class = run_test_page.visible_element_get_class(RunTestPageLocators.TC_1ST_STEP_FAILED_BTN)
    assert 'active' in failed_class and 'focus' not in failed_class\
        and status == '❌  Failed', "Status should be 'Failed' for test case"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_set_case_status_blocked(browser, login, logout):
    """Set 'Blocked' test case status"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.set_case_status('blocked')
    status = run_test_page.get_case_status()
    assert status == '🚫  Blocked', "Status should be 'Blocked' for test case"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_set_case_status_blocked_and_save_close(browser, login, logout):
    """Set 'Blocked' test case status and save and open case status on 'Cases' page"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.set_case_status('blocked')
    run_test_page.save_btn_click()
    status = run_test_page.get_case_status()
    run_test_page.back_to_suite_btn_click()
    run_test_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    case_status = cases_page.get_first_case_status()
    assert status == '🚫  Blocked'\
        and status == case_status, "Status should be 'Blocked' for test case"


@pytest.mark.main
def test_set_case_status_pause(browser, login, logout):
    """Set 'Pause' test case status"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.set_case_status('pause')
    status = run_test_page.get_case_status()
    assert status == '⏸  Pause', "Status should be 'Pause' for test case"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_set_case_status_pause_and_save_close(browser, login, logout):
    """Set 'Pause' test case status and save and check case status on 'Cases' page"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.set_case_status('pause')
    run_test_page.save_btn_click()
    status = run_test_page.get_case_status()
    run_test_page.back_to_suite_btn_click()
    run_test_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    case_status = cases_page.get_first_case_status()
    assert status == '⏸  Pause' \
        and status == case_status, "Status should be 'Pause' for test case"


@pytest.mark.main
def test_set_case_status_passed(browser, login, logout):
    """Set 'Passed' test case status"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.failed_btn_1_step_click()
    run_test_page.set_case_status('passed')
    status = run_test_page.get_case_status()
    assert status == '✅  Passed', "Status should be 'Passed' for test case"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_set_case_status_passed_and_save_close(browser, login, logout):
    """Set 'Passed' test case status and save and check case status on 'Cases' page"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.failed_btn_1_step_click()
    run_test_page.set_case_status('passed')
    run_test_page.save_btn_click()
    status = run_test_page.get_case_status()
    run_test_page.back_to_suite_btn_click()
    run_test_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    case_status = cases_page.get_first_case_status()
    assert status == '✅  Passed' \
        and status == case_status, "Status should be 'Pause' for test case"


@pytest.mark.main
def test_set_case_status_failed(browser, login, logout):
    """Set 'Failed' test case status"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.passed_btn_1_step_click()
    run_test_page.set_case_status('failed')
    status = run_test_page.get_case_status()
    assert status == '❌  Failed', "Status should be 'Failed' for test case"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_set_case_status_failed_and_save_close(browser, login, logout):
    """Set 'Failed' test case status and save and check case status on 'Cases' page"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.passed_btn_1_step_click()
    run_test_page.set_case_status('failed')
    run_test_page.save_btn_click()
    status = run_test_page.get_case_status()
    run_test_page.back_to_suite_btn_click()
    run_test_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    case_status = cases_page.get_first_case_status()
    assert status == '❌  Failed' \
        and status == case_status, "Status should be 'Failed' for test case"


@pytest.mark.main
def test_case_status_should_changed_if_fail_step(browser, login, logout):
    """Check that case status changed to 'Failed' if failed one step"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.passed_btn_1_step_click()
    run_test_page.failed_btn_1_step_click()
    status = run_test_page.get_case_status()
    assert status == '❌  Failed', "Status should be 'Failed' for test case"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_click_all_passed_buttons_case_status_passed(browser, login, logout):
    """Check that case status is 'Passed' if click all 'Passed' buttons"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.click_all_passed_btns()
    status = run_test_page.get_case_status()
    assert status == '✅  Passed', "Status should be 'Passed' for test case"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_click_all_failed_buttons_case_status_failed(browser, login, logout):
    """Check that case status is 'Failed' if click all 'Failed' buttons"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.click_all_failed_btns()
    status = run_test_page.get_case_status()
    assert status == '❌  Failed', "Status should be 'Passed' for test case"
    run_test_page.back_to_suite_btn_click()


@pytest.mark.main
def test_click_random_failed_button_case_status_failed(browser, login, logout):
    """Check that case status is 'Failed' if click random 'Fail' button"""
    open_run_test_page_for_1st_test(browser)
    run_test_page = RunTestPage(browser)
    run_test_page.click_random_failed_btn()
    status = run_test_page.get_case_status()
    assert status == '❌  Failed', "Status should be 'Passed' for test case"
    run_test_page.back_to_suite_btn_click()





















