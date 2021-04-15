import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.welcome_page import WelcomePage
from utils.constants import DEFAULT_WAIT_TIME, LOGIN, PASSWORD
from locators import locators
from selenium.webdriver.chrome.options import Options
import psycopg2
from utils.constants import *
import  time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    options = Options()
#    options.add_argument('--headless')
#    options.add_argument('--enable-javascript')
#    options.add_argument('--disable-gpu')
#   #options.add_argument('--window-size=2560x2160') # Set display resolution
#    options.add_argument('--window-size=3840x2160')
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(DEFAULT_WAIT_TIME)
    browser.maximize_window()
    failed_before = request.session.testsfailed  # for screenshots
    yield browser
    if request.session.testsfailed != failed_before:  # for screenshots
        take_screenshot(browser)  # for screenshots
    print(f"\nquit {browser_name} browser..", )
    browser.quit()


def take_screenshot(browser):
    screenshots_dir = "D:\\Reports\\Auto_tests\\"
    test_case_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    screenshot_time_id = test_case_name + "_" + time.strftime("%Y-%m-%d-%H-%M-%S")
    screenshot_file_path = screenshots_dir + screenshot_time_id + ".png"
    browser.save_screenshot(screenshot_file_path)


@pytest.fixture(scope="function")
def login(browser):
    """ Login method for each test
            default creds from local file will be set in test's first page"""
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.input_text_in_username_tb_in(LOGIN)
    welcome_page.input_text_in_password_tb_in(PASSWORD)
    welcome_page.sign_in_btn_in_click()


@pytest.fixture(scope="function")
def logout(browser):
    """ Logout method for each test
        'Hello,User' options-> 'Logout' will be executed in test's last page"""
    yield logout
    browser.get(browser.current_url)  # load current URL _driver
    try:
        wait = WebDriverWait(browser, DEFAULT_WAIT_TIME)  # driver
        wait.until(EC.visibility_of_element_located(locators.BasePageLocators.HELLO_USER_DPDN)).click()
        wait.until(EC.visibility_of_element_located(locators.BasePageLocators.LOGOUT_OPT)).click()
    except Exception as e:
        print("error occurred in logout", e)
    finally:
        pass


@pytest.fixture(scope="function")
def close(browser):
    """ Delete cookies method for each test to skip logout"""
    yield close
    try:
        browser.delete_all_cookies()
    except Exception as e:
        print("error occurred", e)
    finally:
        pass


@pytest.fixture(scope="function")
def delete_temp_user():
    """ Delete temp user from DB and update 'Invite Code'"""
    yield close
    con = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
    cur = con.cursor()
    try:
        cur.execute('DELETE FROM "user" WHERE username = %s', (TEMP_USER,))
        print(f"\nTemp User {TEMP_USER} deleted. Total deleted rows:{cur.rowcount}")
        cur.execute('UPDATE "INVITE_INFO" SET "ACTIVATED"=null WHERE "ID"=%s;', [36])
        print("Invite code updated")
    except Exception as e:
        print("error occurred", e)
    con.commit()
    cur.close()
    # close DB connection
    con.close()
    print("Database closed successfully")


""" Read test data from file: 
Login
Password
Search test case
"""
with open('test_data/input.txt', 'r') as f:
    lines = f.read().splitlines()
PARAMS_LOGIN = str(lines[0])
PARAMS_PASSWORD = str(lines[1])
PARAMS_SEARCH_TC = str(lines[2])


@pytest.fixture(params=PARAMS_LOGIN.split(','))
def parametrized_username(request):
    return request.param


@pytest.fixture(params=PARAMS_PASSWORD.split(','))
def parametrized_password(request):
    return request.param


@pytest.fixture(params=PARAMS_SEARCH_TC.split(','))
def search_test_case(request):
    return request.param
