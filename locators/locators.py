from selenium.webdriver.common.by import By


class WelcomePageLocators:
    #WELCOME_URL = "http://127.0.0.1:5000/login?next=%2F"
    WELCOME_URL = "https://trunner.herokuapp.com/login?next=%2Fsuites"
    ABOUT_US_BTN = (By.CSS_SELECTOR, ".content-logo [href='/about']")
    SIGN_UP_BTN_IN = (By.CSS_SELECTOR, "[class='container'] #sign-up-btn")
    SIGN_IN_BTN_IN = (By.CSS_SELECTOR, "[class='container'] .sign-in-form [type='submit']")
    USER_NAME_TB_IN = (By.CSS_SELECTOR, "[class='container'] .sign-in-form [name=username]")
    PASSWORD_TB_IN = (By.CSS_SELECTOR, "[class='container'] .sign-in-form [name=password]")
    SIGN_UP_BTN_UP = (By.ID, "signup")
    SIGN_IN_BTN_UP = (By.ID, "sign-in-btn")
    USER_NAME_TB_UP = (By.ID, "username")
    TOKEN_TB_UP = (By.ID, "token")
    INVITE_TB_UP = (By.ID, "invite")
    PASSWORD_TB_UP = (By.ID, "password")
    INVALID_CRED_ERROR = (By.CSS_SELECTOR, ".notification.is-danger")


class AboutPageLocators:
    #ABOUT_URL = "http://127.0.0.1:5000/about"
    ABOUT_URL = "https://trunner.herokuapp.com/about"
    ABOUT_TITLE = 'About'
    TRUNNER_LNK =(By.CSS_SELECTOR, "nav a.navbar-brand")
    ADD_SUITE_LNK=(By.CSS_SELECTOR, "ul li a[href='/suites']")

    HELLO_USER_DPDN=(By.CSS_SELECTOR, "#navbarDropdownMenuLink")
    SETTINGS_OPT=(By.CSS_SELECTOR, "div a.dropdown-item[href='/settings']")
    SETTINGS_OPT_NAMES=(By.CSS_SELECTOR, "a.dropdown-item")
    LOGOUT_OPT=(By.CSS_SELECTOR, "a[href='/logout']")
    NAVBAR=(By.CSS_SELECTOR, "ul>li[class='nav-item active']")
    TRUNNER_CARD=(By.CSS_SELECTOR, "div.pricing-header")


class SettingsPageLocators:
    #SETTINGS_URL = "http://127.0.0.1:5000/settings"
    SETTINGS_URL = "https://trunner.herokuapp.com/settings"
    TRUNNER_LNK = (By.CSS_SELECTOR, ".navbar-brand")
    TEST_SUITES_LNK = (By.CSS_SELECTOR, ".nav-link[href='/suites']")
    SUITES_MANAGER_LNK = (By.CSS_SELECTOR, ".nav-link[href='/suites_manager']")  #
    ABOUT_LNK = (By.CSS_SELECTOR, ".nav-link[href='/about']")
    TOKEN_TB = (By.ID, "token")
    NEW_PASSWORD_TB = (By.ID, "newPass")
    CONFIRM_PASSWORD_TB = (By.ID, "newPassConfirm")
    UPDATE_TOKEN_BTN = (By.ID, "save")
    UPDATE_PASSWORD_BTN = (By.ID, "savePassword")

    HELLO_USER_DPDN = (By.ID, "navbarDropdownMenuLink")
    SETTINGS_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/settings']")
    LOGOUT_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/logout']")


class SuitesPageLocators:
    SUITES_URL = "https://trunner.herokuapp.com/suites"
    #SUITES_URL = "http://127.0.0.1:5000/suites"
    TRUNNER_LNK = (By.CSS_SELECTOR, ".navbar-brand")
    TEST_SUITES_LNK = (By.CSS_SELECTOR, ".nav-link[href='/suites']")
    SUITES_MANAGER_LNK = (By.CSS_SELECTOR, ".nav-link[href='/suites_manager']")  #
    ABOUT_LNK = (By.CSS_SELECTOR, ".nav-link[href='/about']")

    HELLO_DPDN = (By.ID, "navbarDropdownMenuLink")
    SETTINGS_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/settings']")
    LOGOUT_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/logout']")

    ADD_SUITE_BTN = (By.ID, "addSuite")
    SUITE_REPORT_OPT = (By.CSS_SELECTOR, ".custom-menu li[data-action='suite-report']")
    ADO_EXPORT_OPT = (By.CSS_SELECTOR, ".custom-menu li[data-action='ado-export']")
    DELETE_SUITE_OPT = (By.CSS_SELECTOR, ".custom-menu li[data-action='delete-suite']")

    """First row data (1st iteration)"""
    SUITE_1_LNK = (By.CSS_SELECTOR, ".clickable-row:first-child .suite-link")
    TEST_CASES_VALUE = (By.CSS_SELECTOR, ".clickable-row:first-child td:nth-of-type(2)")
    PASSED_1_DPDN = (By.CSS_SELECTOR, ".clickable-row:first-child [data-target^='#passed'] p")
    FAILED_1_DPDN = (By.CSS_SELECTOR, ".clickable-row:first-child [data-target^='#failed'] p")
    BLOCKED_1_DPDN = (By.CSS_SELECTOR, ".clickable-row:first-child [data-target^='#blocked'] p")
    NOT_EXECUTED_1_VALUE = (By.CSS_SELECTOR, ".clickable-row:first-child td:nth-of-type(6)")
    CREATED_BY_1_VALUE = (By.CSS_SELECTOR, ".clickable-row:first-child td:nth-of-type(7)")
    CREATED_DATE_1_VALUE = (By.CSS_SELECTOR, ".clickable-row:first-child td:last-child")
    TEST_CASE_COUNT = (By.CSS_SELECTOR, "tbody tr[class=clickable-row]")
    PASSED_TC_1_1_LNK = (By.CSS_SELECTOR, "[class='clickable-row']:first-child+tr [id^='passed'] a")
    FAILED_TC_1_1_LNK = (By.CSS_SELECTOR, "[class='clickable-row']:first-child+tr [id^='failed'] a")
    BLOCKED_TC_1_1_LNK = (By.CSS_SELECTOR, "[class='clickable-row']:first-child+tr [id^='blocked'] a")


class TestSuitePageLocators:
    TRUNNER_LNK = (By.CSS_SELECTOR, ".navbar-brand")
    TEST_SUITES_LNK = (By.CSS_SELECTOR, ".nav-link[href='/suites']")
    SUITES_MANAGER_LNK = (By.CSS_SELECTOR, ".nav-link[href='/suites_manager']")  #
    ABOUT_LNK = (By.CSS_SELECTOR, ".nav-link[href='/about']")
    RUN_TEST_BTN = (By.ID, "runCase")
    STATISTICS_BTN = (By.ID, "statCase")
    CURRENT_SUITE_NAME = (By.CSS_SELECTOR, ".navbar-collapse [class='nav-link']")

    HELLO_DPDN = (By.CSS_SELECTOR, ".nav-link#navbarDropdownMenuLink")
    SETTINGS_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/settings']")
    LOGOUT_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/logout']")

    """First row data (1st iteration)"""
    CASE_ID_LNK = (By.CSS_SELECTOR, "tbody .clickable-row:first-child .tcid a")
    CASE_NAME = (By.CSS_SELECTOR, "tbody .clickable-row:first-child td:nth-child(2) p")
    CASE_STATE = (By.CSS_SELECTOR, "tbody .clickable-row:first-child .testCaseState p")
    TESTER_NAME = (By.CSS_SELECTOR, "tbody .clickable-row:first-child .centered p")

    """MB3 options for active row"""
    ACTIVE_1ST_ROW = (By.CSS_SELECTOR, "tbody .clickable-row:first-child td:nth-child(2)")
    RUN_TEST_OPT_LNK = (By.CSS_SELECTOR, "body .custom-menu-tclist [data-action=run-test] .run_tc_mb3")
    STATISTICS_OPT_LNK = (By.CSS_SELECTOR, "body .custom-menu-tclist .show_stat_mb3")

    ASSIGN_OPT_LNK = (By.CSS_SELECTOR, "body .custom-menu-tclist [data-action=assign-to] #assign-to-a")
    ASSIGN_TO_USER_COUNT = (By.CSS_SELECTOR, "body .assign-to-submenu li")
    ASSIGN_TO_1ST_USER = (By.CSS_SELECTOR, "body .assign-to-submenu .user-to-set:first-child")
    ASSIGN_TO_LAST_USER = (By.CSS_SELECTOR, "body .assign-to-submenu .user-to-set:last-child")


class SuiteManagerPageLocators:
    SUITE_MANAGER_PAGE_LNK = "https://trunner.herokuapp.com/suites_manager"
    TRUNNER_LNK = (By.CSS_SELECTOR, ".navbar-brand")
    TEST_SUITES_LNK = (By.CSS_SELECTOR, ".nav-link[href='/suites']")
    SUITES_MANAGER_LNK = (By.CSS_SELECTOR, ".nav-link[href='/suites_manager']")  #
    ABOUT_LNK = (By.CSS_SELECTOR, ".nav-link[href='/about']")

    SUITE_SELECTOR_DPDN = (By.CSS_SELECTOR, ".form-control#suites-selector")
    SUITES_COUNT_OPT = (By.CSS_SELECTOR, ".form-control#suites-selector .select-option")
    SUITE_1ST_OPT = (By.CSS_SELECTOR, ".form-control#suites-selector .select-option:first-child")
    SUITE_LAST_OPT = (By.CSS_SELECTOR, ".form-control#suites-selector .select-option:last-child")

    ADD_CASE_TO_SUITE_BTN = (By.CSS_SELECTOR, ".nav-link[data-target='#addCaseToSuite']")
    DELETE_CASE_FROM_SUITE_BTN = (By.CSS_SELECTOR, ".nav-link#deleteCaseFromSuite")

    CREATE_SUITE_DPDN = (By.CSS_SELECTOR, ".nav-link.suite-create")
    FROM_ADO_QUERY_OPT = (By.CSS_SELECTOR, ".dropdown-item[data-target='#addFromAdoQuery']")
    EMPTY_SUITE_OPT = (By.CSS_SELECTOR, ".dropdown-item[data-target='#createEmptySuite']")
    FROM_EXIST_SUITE_OPT = (By.CSS_SELECTOR, ".dropdown-item[data-target='#copyFromExistingSuite']")

    HELLO_DPDN = (By.CSS_SELECTOR, "[class='nav-link dropdown-toggle']#navbarDropdownMenuLink")
    SETTINGS_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/settings']")
    LOGOUT_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/logout']")

    TC_COUNT = (By.CSS_SELECTOR, ".table .test_case_row")

    """First row data """
    USE_1ST_TC_CHKBX = (By.CSS_SELECTOR, ".test_case_row:first-of-type .checked_tc")
    ID_1ST_TC_VALUE = (By.CSS_SELECTOR, ".test_case_row:first-of-type .tcid")
    TEST_CASE_1ST_TITLE = (By.CSS_SELECTOR, ".test_case_row:first-of-type td:last-child")

    """Last row data """
    USE_LAST_TC_CHKBX = (By.CSS_SELECTOR, ".test_case_row:last-of-type .checked_tc")
    ID_LAST_TC_VALUE = (By.CSS_SELECTOR, ".test_case_row:last-of-type .tcid")
    TEST_CASE_LAST_TITLE = (By.CSS_SELECTOR, ".test_case_row:last-of-type td:last-child")


class RunTestPageLocators:
    TRUNNER_LNK = (By.CSS_SELECTOR, ".navbar-brand")
    SAVE_BTN = (By.CSS_SELECTOR, ".test_case_row:first-of-type .tcid")
    SAVE_AND_CLOSE_BTN = (By.CSS_SELECTOR, ".nav-link#saveResultClose")
    REPORT_BUG_BTN = (By.CSS_SELECTOR, ".nav-link[href$='create/bug']")
    INFO_ICON = (By.CSS_SELECTOR, ".nav-link .help-icon")
    BACK_TO_SUITE_BTN = (By.CSS_SELECTOR, ".nav-link#backToSuite")

    TC_TITLE = (By.CSS_SELECTOR, ".col-md-10")

    TC_STATUS_DPDN = (By.CSS_SELECTOR, ".col-md-2 #testStatus")
    TC_STATUS_OPT = (By.CSS_SELECTOR, ".col-md-2 #testStatus option:first-child")
    TC_PASSED_OPT = (By.CSS_SELECTOR, ".col-md-2 #testStatus [value=passed]")
    TC_FAILED_OPT = (By.CSS_SELECTOR, ".col-md-2 #testStatus [value=failed]")
    TC_BLOCKED_OPT = (By.CSS_SELECTOR, ".col-md-2 #testStatus [value=blocked]")
    TC_PAUSED_OPT = (By.CSS_SELECTOR, ".col-md-2 #testStatus [value=paused]")

    TC_STEPS_COUNT = (By.CSS_SELECTOR, "tbody .clickable-row")
    TC_1ST_STEP_ROW = (By.CSS_SELECTOR, "tbody .clickable-row:first-child")
    TC_1ST_STEP_NUMBER = (By.CSS_SELECTOR, "tbody .clickable-row:first-child td:first-child")
    TC_1ST_STEP_DESCRIPTION = (By.CSS_SELECTOR, "tbody .clickable-row:first-child .action")
    TC_1ST_STEP_EXPECTED_RESULT = (By.CSS_SELECTOR, "tbody .clickable-row:first-child .expected")
    TC_1ST_STEP_PASSED_STATUS = (By.CSS_SELECTOR, "tbody .clickable-row:first-child .selector #passed_label")
    TC_1ST_STEP_FAILED_STATUS = (By.CSS_SELECTOR, "tbody .clickable-row:first-child .selector #failed_label")
    TC_1ST_STEP_COMMENT_TB = (By.CSS_SELECTOR, "tbody .clickable-row:first-child [id^=exampleForm]")
    TC_1ST_STEP_COMMENT_TB_LABEL = (By.CSS_SELECTOR, "tbody .clickable-row:first-child [for^=exampleForm]")

    TC_LAST_STEP_NUMBER = (By.CSS_SELECTOR, "tbody .clickable-row:last-child td:first-child")
    TC_LAST_STEP_DESCRIPTION = (By.CSS_SELECTOR, "tbody .clickable-row:last-child .action")
    TC_LAST_STEP_EXPECTED_RESULT = (By.CSS_SELECTOR, "tbody .clickable-row:last-child .expected")
    TC_LAST_STEP_PASSED_STATUS = (By.CSS_SELECTOR, "tbody .clickable-row:last-child .selector #passed_label")
    TC_LAST_STEP_FAILED_STATUS = (By.CSS_SELECTOR, "tbody .clickable-row:last-child .selector #failed_label")
    TC_LAST_STEP_COMMENT_TB = (By.CSS_SELECTOR, "tbody .clickable-row:last-child [id^=exampleForm]")
    TC_LAST_STEP_COMMENT_TB_LABEL = (By.CSS_SELECTOR, "tbody .clickable-row:last-child [for^=exampleForm]")

    HELLO_DPDN = (By.ID, "[class='nav-link dropdown-toggle']#navbarDropdownMenuLink")
    SETTINGS_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/settings']")
    LOGOUT_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/logout']")