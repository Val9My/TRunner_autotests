from selenium.webdriver.common.by import By


class WelcomePageLocators:
    #WELCOME_URL = "http://127.0.0.1:5000/login?next=%2F"
    WELCOME_URL = "https://trunner.herokuapp.com/login?next=%2Fsuites"
    ABOUT_US_BTN = (By.XPATH, "//a[contains(text(),'About Us')]")  # //a[@href='/about']
    SIGN_UP_BTN_IN = (By.ID, "sign-up-btn")
    SIGN_IN_BTN_IN = (By.XPATH, "//form[@class='sign-in-form']//input[@value='Sign In']")
    USER_NAME_TB_IN = (By.XPATH, "//form[@class='sign-in-form']//input[@name='username']")
    PASSWORD_TB_IN = (By.XPATH, "//form[@class='sign-in-form']//input[@name='password']")
    SIGN_UP_BTN_UP = (By.ID, "signup")
    SIGN_IN_BTN_UP = (By.ID, "sign-in-btn")
    USER_NAME_TB_UP = (By.ID, "username")
    TOKEN_TB_UP = (By.ID, "token")
    INVITE_TB_UP = (By.ID, "invite")
    PASSWORD_TB_UP = (By.ID, "password")
    INVALID_CRED_ERROR = (By.XPATH, "//div[contains(text(), 'Invalid credentials')]")


class AboutPageLocators:
    #ABOUT_URL = "http://127.0.0.1:5000/about"
    ABOUT_URL = "https://trunner.herokuapp.com/about"
    ABOUT_TITLE = 'About'
    TRUNNER_LNK = (By.XPATH, "//a[@class='navbar-brand'][@href='/suites']")
    ADD_SUITE_LNK = (By.XPATH, "//a[@class='nav-link'][@href='/suites']")  # //a[contains(text(),'Add Suite')]
    AVAILABLE_SUITES_LNK = (By.XPATH, "//a[@class='nav-link'][@href='/suitify']")  # //a[contains(text(),'Available
    # Suites')]
    HELLO_USER_DPDN = (By.ID, "navbarDropdownMenuLink")
    SETTINGS_OPT = (By.XPATH, "//a[@href='/settings']")  # //a[contains(text(),'Settings')]
    LOGOUT_OPT = (By.XPATH, "//a[@href='/logout'] ")  # //a[contains(text(),'Logout')]


class SettingsPageLocators:
    #SETTINGS_URL = "http://127.0.0.1:5000/settings"
    SETTINGS_URL = "https://trunner.herokuapp.com/settings"
    TRUNNER_LNK = (By.XPATH, "//a[@class='navbar-brand'][@href='/suites']")
    ADD_SUITE_LNK = (By.XPATH, "//a[@class='nav-link'][@href='/suites']")  # //a[contains(text(),'Add Suite')]
    AVAILABLE_SUITES_LNK = (By.XPATH, "//a[@class='nav-link'][@href='/suitify']")  #
    ABOUT_LNK = (By.XPATH, "//a[@class='nav-link'][@href='/about']")  # //a[contains(text(),'About')]
    TOKEN_TB = (By.ID, "token")
    NEW_PASSWORD_TB = (By.ID, "newPass")
    CONFIRM_PASSWORD_TB = (By.ID, "newPassConfirm")
    UPDATE_TOKEN_BTN = (By.ID, "save")
    UPDATE_PASSWORD_BTN = (By.ID, "savePassword")
    HELLO_USER_DPDN = (By.ID, "navbarDropdownMenuLink")
    SETTINGS_DPDN_ITEM = (By.XPATH, "//a[@class='dropdown-item' and contains(text(),'Settings')]")
    LOGOUT_DPDN_ITEM = (By.XPATH, "//a[@class='dropdown-item' and contains(text(),'Logout')]")



class SuitesPageLocators:
    SUITES_URL = "https://trunner.herokuapp.com/suites"
    #SUITES_URL = "http://127.0.0.1:5000/suites"
    TRUNNER_LNK = (By.XPATH, "//a[@class='navbar-brand']")
    ADD_SUITE_LNK = (By.XPATH, "//a[@class='nav-link'][@href='/suites']")  # //a[contains(text(),'Add Suite')]
    AVAILABLE_SUITES_LNK = (By.XPATH, "//a[@class='nav-link'][@href='/suitify']")
    ABOUT_LNK = (By.XPATH, "//a@class='nav-link'][@href='/about']")
    HELLO_DPDN = (By.ID, "navbarDropdownMenuLink")
    SETTINGS_OPT = (By.XPATH, "//a[@href='/settings']")
    LOGOUT_OPT = (By.XPATH, "//a[@href='/logout'] ")
    ADD_SUITE_BTN = (By.ID, "addSuite")
    SELECT_TEST_SUITE_BTN = (By.XPATH, "//button[contains(text(),'Test Suite')]")
    QUERY_ID_TB = (By.XPATH, "//input[@name='query_id']")
    TEST_SUITES_CB = (By.ID, "select2-test_suites-wj-container")
    SUIT_REPORT_DPDN_ITEM = (By.XPATH, "//ul[@class='custom-menu']/li[contains(text(),'Suite Report')]")
    EXPORT_TO_ADO_DPDN_ITEM = (By.XPATH, "//ul[@class='custom-menu']/li[contains(text(),'Export to ADO')]")
    DELETE_SUITE_DPDN_ITEM = (By.XPATH, "//ul[@class='custom-menu']/li[contains(text(),'Delete Suite')]")
    """First row data (1st iteration)"""
    SUITE_1_LNK = (By.XPATH, "//tbody/tr[@class='clickable-row'][1]/td[@class='suite-link']/child::a")
    TEST_CASES_VALUE = (By.XPATH, "//tr[@class='clickable-row'][1]/td[@class='suite-link']/following::p[1]")
    PASSED_1_DPDN = (By.XPATH, "//tr[@class='clickable-row'][1]/child::td[3]")
    FAILED_1_DPDN = (By.XPATH, "//tr[@class='clickable-row'][1]/child::td[4]")
    BLOCKED_1_DPDN = (By.XPATH, "//tr[@class='clickable-row'][1]/child::td[5]")
    NOT_EXECUTED_1_VALUE = (By.XPATH, "//tr[@class='clickable-row'][1]/child::td[6]")
    CREATED_BY_1_VALUE = (By.XPATH, "//tr[@class='clickable-row'][1]/child::td[7]")
    CREATED_DATE_1_VALUE = (By.XPATH, "//tr[@class='clickable-row'][1]/child::td[8]")
    FAILED_TC_1_1_LNK = (By.XPATH, "//td[@class='subtr hiddenRow']//a[@class='text-dark substat-failed']//parent::div")


class AvailableSuitesPageLocators:
    AVAILABLE_SUITS_URL = "http://127.0.0.1:5000/suitify"
    TRUNNER_LNK = (By.XPATH, "//a[@class='navbar-brand'][@href='/suites']")
    ADD_SUITE_LNK = (By.XPATH, "//a[@class='nav-link'][@href='/suites']")  # //a[contains(text(),'Add Suite')]
    AVAILABLE_SUITES_LNK = (By.XPATH, "//a[@class='nav-link'][@href='/suitify']")
    ABOUT_LNK = (By.XPATH, "//a[@class='nav-link'][@href='/about']")
    HELLO_DPDN = (By.ID, "navbarDropdownMenuLink")
    SUITE_LINK = (By.XPATH, "//a[@href='/cases/1']")


class TestSuitePageLocators:

    TRUNNER_LNK = (By.XPATH, "//a[@class='navbar-brand']")
    Test_Suites_LNK = (By.XPATH, "//a[@class='nav-link' and contains(text(),'Test Suites')]")
    SUITE_MANAGER_LNK = (By.XPATH, "//a[@class='nav-link' and contains(text(),'Suite Manager')]")
    ABOUT_LNK = (By.XPATH, "//a[@class='nav-link' and contains(text(),'About')]")
    CURRENT_SUITE_NAME = (By.XPATH, "//a[@class='nav-link' and contains(text(),'Current Suite')]")
    HELLO_DPDN = (By.ID, "navbarDropdownMenuLink")
    SETTINGS_OPT = (By.XPATH, "//a[@href='/settings']")
    LOGOUT_OPT = (By.XPATH, "//a[@href='/logout'] ")
    """First row data (1st iteration)"""
    TEST_CASE_ID_LNK = (By.XPATH, "//tr[@class='clickable-row'][1]/td[@class='tcid']")
    TEST_CASE_NAME = (By.XPATH, "///tr[@class='clickable-row'][1]/td[@class='tcid']/following-sibling::td[1]") # /p
    TEST_CASE_STATE = (By.XPATH, "//tr[@class='clickable-row'][1]/td[@class='tcid']/following-sibling::td[2]/p")
    TESTER_NAME = (By.XPATH, "//tr[@class='clickable-row'][1]/td[@class='tcid']/following-sibling::td[3]//p")
    """Clickable row active for MB3 options"""
    ACTIVE_ROW = (By.XPATH, "//tr[@class='clickable-row active']")
    RUN_TEST_OPT_LNK = (By.XPATH, "//ul[@class='custom-menu-tclist']/li[@data-action='run-test']")
    STATISTICS_OPT_LNK = (By.XPATH, "//ul[@class='custom-menu-tclist']/li[@data-action='show-statistics']")
    ASSIGN_OPT_LNK = (By.XPATH, "//ul[@class='custom-menu-tclist']/li[@data-action='assign-to']")





