import time
import pytest
from locators import locators
from pages.cases_page import CasesPage
from pages.run_test_page import RunTestPage
from pages.suites_info_page import SuitesPage


@pytest.mark.cases
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

@pytest.mark.cases
def test_run_test_option_is_seen(browser, login, logout):
    """Check that Run Test option is visible after clicking on case"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    assert cases_page.is_element_seen(locators.CasesPageLocators.RUN_TEST_BTN)

@pytest.mark.cases
def test_run_test_btn(browser, login, logout):
    """Check that Run Test option is redirecting user to the Run Page"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.run_test_btn_click()
    assert browser.current_url == "https://trunner.herokuapp.com/run/26/754"


@pytest.mark.cases
def test_statistics_option_is_seen(browser, login, logout):
    """Check that Statistics option is visible after clicking on case"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    assert cases_page.is_element_seen(locators.CasesPageLocators.STATISTICS_BTN)

@pytest.mark.cases
def test_current_suite_name(browser, login, logout):
    """Check that Current suite name is visible and contains correct information.
    Expected result: Current Suite - Nadiia - Linux - 20.6.4"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    current_suite_name = cases_page.visible_element_get_text(locators.CasesPageLocators.CURRENT_SUITE_NAME)
    assert current_suite_name == "Current Suite - Nadiia - Linux - 20.6.4\n(current)"


@pytest.mark.cases
def test_cases_dropdown(browser, login, logout):
    """Check that the font sizes are the same in the dropdown custom options menu"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.click_mb3_first_case()
    font_sizes = [cases_page.get_css_property(locators.CasesPageLocators.RUN_TEST_OPT_LNK, "font-size"), \
                  cases_page.get_css_property(locators.CasesPageLocators.STATISTICS_OPT_LNK, "font-size"), \
                  cases_page.get_css_property(locators.CasesPageLocators.ASSIGN_OPT_LNK, "font-size")]
    assert font_sizes == ['14px', '14px', '14px']


@pytest.mark.cases
def test_statistics_table_location_and_size(browser, login, logout):
    """Check that Statistics table is opening  in the correct size and position"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.click_statistics_option()
    assert cases_page.get_element_size(locators.CasesPageLocators.STATTABLE) == {'height': 47, 'width': 339} and \
           cases_page.get_element_location(locators.CasesPageLocators.STATTABLE) == {'x': 845, 'y': 70}

@pytest.mark.cases
def test_statistics_table_styles(browser, login, logout):
    """Check that Statistics table is opening  with correct styles"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.click_statistics_option()
    font_size = cases_page.get_css_property(locators.CasesPageLocators.STATTABLE, 'font-size')
    font_weight = cases_page.get_css_property(locators.CasesPageLocators.STATTABLE, 'font-weight')
    line_height = cases_page.get_css_property(locators.CasesPageLocators.STATTABLE, 'line-height')
    font_family = cases_page.get_css_property(locators.CasesPageLocators.STATTABLE, 'font-family')
    webkit_text_size_adjust = cases_page.get_css_property(locators.CasesPageLocators.STATTABLE,
                                                          'webkit-text-size-adjust')
    assert [font_size, font_weight, line_height, font_family, webkit_text_size_adjust] == ['14px', '400', '21px',
                                                                                           'Poppins, Arial, "Helvetica Neue", sans-serif',
                                                                                           '100%']


@pytest.mark.cases
def test_statistics_table_scenario1(browser, login, logout):
    """Check that Statistics table contains required fields"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.click_statistics_option()
    assert cases_page.is_element_seen(locators.CasesPageLocators.STATTABLE) and \
           cases_page.is_element_seen(locators.CasesPageLocators.STATTABLE_SUITE) and \
           cases_page.is_element_seen(locators.CasesPageLocators.STATTABLE_RUN_BY) and \
           cases_page.is_element_seen(locators.CasesPageLocators.STATTABLE_RESULT) and \
           cases_page.is_element_seen(locators.CasesPageLocators.STATTABLE_DURATION) and \
           cases_page.is_element_seen(locators.CasesPageLocators.STATTABLE_DATE)


@pytest.mark.cases
def test_statistics_table_scenario2(browser, login, logout):
    """Check that Statistics table contains correct information"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.run_test_btn_click()
    run_test_page = RunTestPage(browser)
    run_test_page.wait_new_page_load()
    run_test_page.set_case_status('passed')
    run_test_page.save_btn_click()
    run_test_page.back_to_suite_btn_click()
    run_test_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.click_statistics_option()
    assert cases_page.visible_element_get_text(
        locators.CasesPageLocators.STATTABLE_SUITE) == "Nadiia - Linux - 20.6.4" and \
           cases_page.visible_element_get_text(locators.CasesPageLocators.STATTABLE_RUN_BY) == "KYahorlytska" and \
           cases_page.visible_element_get_text(locators.CasesPageLocators.STATTABLE_RESULT) == "✅  Passed" and \
           cases_page.visible_element_get_text(locators.CasesPageLocators.STATTABLE_DURATION) <= "00:00:05" and \
           cases_page.visible_element_get_text(
               locators.CasesPageLocators.STATTABLE_DATE) == "Dec 28 2020 09:37:52"  # defect,should be changed to current date


@pytest.mark.cases
def test_statistics_table_scenario3(browser, login, logout):
    """Check that Statistics table is updated if switch between several cases"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.click_statistics_option()
    cases_page.click_nth_case(7)
    cases_page.click_statistics_option()
    time.sleep(2)
    assert cases_page.visible_element_get_text(locators.CasesPageLocators.STATTABLE_SUITE) == "Nadiia - Linux - 20.6.4" and \
           cases_page.visible_element_get_text(locators.CasesPageLocators.STATTABLE_RUN_BY) == "Nadiia" and \
           cases_page.visible_element_get_text(locators.CasesPageLocators.STATTABLE_RESULT) == "❌  Failed"

@pytest.mark.cases
def test_cases_info_scenario1(browser, login, logout):
    """Check that cases info is visible and contains correct information.
    Expected result: Second test case is checking. Id=48697, Naming is
    Validate that user A gets notification with changes in 'Sessions' view, when user B renames an editor
    Tester is Nadiia, State is Passed"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    second_case_id = cases_page.get_nth_case_id(2)
    second_case_name = cases_page.get_nth_case_name(2)
    second_case_tester_name = cases_page.get_nth_case_tester_name(2)
    second_case_status = cases_page.get_nth_case_status(2)
    assert second_case_id == "48697" and \
           second_case_name == "Validate that user A gets notification with changes in 'Sessions' view, when user B renames an editor." and \
           second_case_tester_name == "Nadiia" and second_case_status == "✅  Passed"

@pytest.mark.cases
def test_cases_info_scenario2(browser, login, logout):
    """Check that cases info is visible and contains correct information.
    Expected result: Second test case is checking. Id=48697, Naming is
     Validate that user A gets notification with changes in 'Sessions' view, when user B renames an editor
     Tester is Nadiia, State is Passed"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    second_case_id = cases_page.get_nth_case_id(2)
    second_case_name = cases_page.get_nth_case_name(2)
    second_case_tester_name = cases_page.get_nth_case_tester_name(2)
    second_case_status = cases_page.get_nth_case_status(2)
    assert second_case_id == "48697" and \
           second_case_name == "Validate that user A gets notification with changes in 'Sessions' view, when user B renames an editor." and \
           second_case_tester_name == "Nadiia" and second_case_status == "✅  Passed"


@pytest.mark.cases
def test_cases_info_scenario3(browser, login, logout):
    """Check that cases info is visible and contains correct information.
    Expected result: Third test case is checking. Id=48698, Naming is
    Validate that user B's session task pane is updated to show the session name in italics when user A delete the same active session
    Tester is Nadiia, State is Passed"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    second_case_id = cases_page.get_nth_case_id(3)
    second_case_name = cases_page.get_nth_case_name(3)
    second_case_tester_name = cases_page.get_nth_case_tester_name(3)
    second_case_status = cases_page.get_nth_case_status(3)
    assert second_case_id == "48698" and \
           second_case_name == "Validate that user B's session task pane is updated to show the session name in italics when user A delete the same active session" and \
           second_case_tester_name == "Nadiia" and second_case_status == "✅  Passed"


@pytest.mark.cases
def test_cases_info_scenario4(browser, login, logout):
    """Check that cases info is visible and contains correct information.
    Expected result: 7th test case is checking. Id=49145, Naming is
     Memory Threshold Warning Dialogue in DSG
     Tester is Nadiia, State is Failed"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    second_case_id = cases_page.get_nth_case_id(7)
    second_case_name = cases_page.get_nth_case_name(7)
    second_case_tester_name = cases_page.get_nth_case_tester_name(7)
    second_case_status = cases_page.get_nth_case_status(7)
    assert second_case_id == "49145" and \
           second_case_name == "Memory Threshold Warning Dialogue in DSG" and \
           second_case_tester_name == "Nadiia" and second_case_status == "❌  Failed"


@pytest.mark.cases
def test_cases_background_color_scenario1(browser, login, logout):
    """"Verify that if cases row is clicked its background color should be grayed out"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    background_color = cases_page.get_css_property(locators.CasesPageLocators.CLICKABLE_ROW, 'background-color')
    assert background_color == "rgba(221, 221, 221, 1)"

@pytest.mark.cases
def test_cases_background_color_scenario2(browser, login, logout):
    """"Verify that if cases row has not been clicked its background color should be whited out"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    background_color = cases_page.get_css_property(locators.CasesPageLocators.CLICKABLE_ROW, 'background-color')
    assert background_color == "rgba(0, 0, 0, 0)"

@pytest.mark.cases
def test_cases_assign_option_scenario1(browser, login, logout):
    """"Verify that if move mouse to the Assign option, list of testers is seen"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.click_mb3_first_case()
    cases_page.move_mouse_on_element(locators.CasesPageLocators.ASSIGN_OPT_LNK)
    assert cases_page.is_element_seen(locators.CasesPageLocators.ASSIGN_SUB_MENU)

@pytest.mark.cases
def test_cases_assign_option_scenario2(browser, login, logout):
    """"Verify that if move mouse to the Assign option and then re-clicking in another position relatively, the list of tester should not be seen"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.click_mb3_first_case()
    cases_page.move_mouse_on_element(locators.CasesPageLocators.ASSIGN_OPT_LNK)
    cases_page.click_first_case()
    assert not cases_page.is_element_seen(
        locators.CasesPageLocators.ASSIGN_SUB_MENU)  # defect: the list of testers is still seen


@pytest.mark.cases
def test_cases_assign_option_scenario3(browser, login, logout):
    """"Verify re-assignment tester for test case"""
    suites_page = SuitesPage(browser)
    suites_page.wait_new_page_load()
    suites_page.suite_1st_link_click()
    suites_page.wait_new_page_load()
    cases_page = CasesPage(browser)
    cases_page.click_first_case()
    cases_page.click_mb3_first_case()
    cases_page.move_mouse_on_element(locators.CasesPageLocators.ASSIGN_OPT_LNK)
    assignment_tester = cases_page.visible_element_get_text(locators.CasesPageLocators.ASSIGN_TO_1ST_USER)
    cases_page.visible_element_click(locators.CasesPageLocators.ASSIGN_TO_1ST_USER)
    first_case_tester = cases_page.get_nth_case_tester_name(1)
    assert assignment_tester == first_case_tester  # defect: unable to change tester
