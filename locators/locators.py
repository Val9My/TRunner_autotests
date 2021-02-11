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
    #TRUNNER_LNK = (By.XPATH, "//a[@class='navbar-brand'][@href='/suites']")
    TRUNNER_LNK =(By.CSS_SELECTOR, "nav a.navbar-brand")
    #ADD_SUITE_LNK = (By.XPATH, "//a[@class='nav-link'][@href='/suites']")  # //a[contains(text(),'Add Suite')]
    ADD_SUITE_LNK=(By.CSS_SELECTOR, "ul li a[href='/suites']")
    AVAILABLE_SUITES_LNK = (By.XPATH, "//a[@class='nav-link'][@href='/suitify']")  # //a[contains(text(),'Available
    # Suites')]
    #HELLO_USER_DPDN = (By.ID, "navbarDropdownMenuLink")  # //a[@id='navbarDropdownMenuLink']
    HELLO_USER_DPDN=(By.CSS_SELECTOR, "#navbarDropdownMenuLink")
    #SETTINGS_OPT = (By.XPATH, "//a[@href='/settings']")  # //a[contains(text(),'Settings')]
    SETTINGS_OPT=(By.CSS_SELECTOR, "div a.dropdown-item[href='/settings']")
    #SETTINGS_OPT_NAMES=(By.XPATH,"//a[@class='dropdown-item']")
    SETTINGS_OPT_NAMES=(By.CSS_SELECTOR, "a.dropdown-item")
    #NAVBAR=(By.XPATH, "//li[@class='nav-item active']")
    NAVBAR=(By.CSS_SELECTOR, "ul>li[class='nav-item active']")
    #LOGOUT_OPT = (By.XPATH, "//a[contains(text(),'Logout')]")  # //a[@href='/logout']
    LOGOUT_OPT=(By.CSS_SELECTOR, "a[href='/logout']")
    #TRUNNER_CARD = (By.XPATH, "//div[contains(@class,'pricing-header')]") #//div[contains(@class,'pricing-header')]
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
    SETTINGS_DPDN_ITEM = (By.CSS_SELECTOR, ".dropdown-item[href='/settings']")
    LOGOUT_DPDN_ITEM = (By.CSS_SELECTOR, ".dropdown-item[href='/logout']")


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
    SUIT_REPORT_DPDN_ITEM = (By.CSS_SELECTOR, ".custom-menu li[data-action='suite-report']")
    EXPORT_TO_ADO_DPDN_ITEM = (By.CSS_SELECTOR, ".custom-menu li[data-action='ado-export']")
    DELETE_SUITE_DPDN_ITEM = (By.CSS_SELECTOR, ".custom-menu li[data-action='delete-suite']")

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
    CURRENT_SUITE_NAME = (By.CSS_SELECTOR, ".navbar-collapse  [class='nav-link']")
    HELLO_DPDN = (By.ID, "navbarDropdownMenuLink")
    SETTINGS_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/settings']")
    LOGOUT_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/logout']")

    """First row data (1st iteration)"""
    TEST_CASE_ID_LNK = (By.CSS_SELECTOR, "tbody .clickable-row:first-child .tcid a")
    TEST_CASE_NAME = (By.CSS_SELECTOR, "tbody .clickable-row:first-child td:nth-child(2) p")
    TEST_CASE_STATE = (By.CSS_SELECTOR, "tbody .clickable-row:first-child .testCaseState p")
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
    TRUNNER_LNK = (By.XPATH, "//a[@class='navbar-brand']")
    TEST_SUITES_LNK = (By.XPATH, "//a[@class='nav-link' and contains(.,'Test Suites')]")
    SUITE_MANAGER_LNK = (By.XPATH, "//a[@class='nav-link' and contains(.,'Suite Manager')]")
    ABOUT_LNK = (By.XPATH, "//a[@class='nav-link' and contains(.,'About')]")
    TEST_SUITES_SELECT_DPDN = (By.ID, "suites-selector")
    TEST_SUITES_SELECT_DPDN_OPT = (By.XPATH, "//select[@id='suites-selector']/option[1]") # 1-st Test-Suite from DPDN
    ADD_CASE_TO_SUITE_BTN = (By.XPATH, "//a[@class='nav-link' and contains(.,'Add')]")
    DELETE_CASE_FROM_SUITE = (By.XPATH, "//a[@class='nav-link' and contains(.,'Delete')]")
    CREATE_SUITE_DPDN = (By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(.,'Create Suite')]")
    CREATE_SUITE_FROM_ADO_OPT = (By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(.,'Create "
                                           "Suite')]/following-sibling::div/a[contains(.,'From ADO')]")
    CREATE_SUITE_EMPTY_SUITE_OPT = (By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(.,'Create "
                                              "Suite')]/following-sibling::div/a[contains(.,'Empty')]")
    CREATE_SUITE_FROM_EXIST_SUITE_OPT = (By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(.,'Create "
                                                   "Suite')]/following-sibling::div/a[contains(.,'Existing Suite')]")
    HELLO_DPDN = (By.ID, "navbarDropdownMenuLink")
    SETTINGS_OPT = (By.XPATH, "//a[@href='/settings']")
    LOGOUT_OPT = (By.XPATH, "//a[@href='/logout'] ")
    """First row data (1st iteration)"""
    USE_CHKBX = (By.XPATH, "//tr[@class='test_case_row'][1]//input[@class='checked_tc'][1]")
    ID_VALUE = (By.XPATH, "//tr[@class='test_case_row'][1]/td[@class='tcid']")
    TEST_CASE_TITLE = (By.XPATH, "//tr[@class='test_case_row'][1]/td[@class='tcid']/following-sibling::td")

class RunTestCasePageLocators:
    TRUNNER_LNK = (By.CSS_SELECTOR, ".navbar-brand")
    TEST_SUITES_LNK = (By.CSS_SELECTOR, ".nav-link[href='/suites']")
    SUITES_MANAGER_LNK = (By.CSS_SELECTOR, ".nav-link[href='/suites_manager']")  #
    ABOUT_LNK = (By.CSS_SELECTOR, ".nav-link[href='/about']")
    CURRENT_SUITE_NAME = (By.CSS_SELECTOR, ".navbar-collapse  [class='nav-link']")
    HELLO_DPDN = (By.ID, "navbarDropdownMenuLink")
    SETTINGS_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/settings']")
    LOGOUT_OPT = (By.CSS_SELECTOR, ".dropdown-item[href='/logout']")