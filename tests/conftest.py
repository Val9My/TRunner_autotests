import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.welcome_page import WelcomePage
from utils.constants import DEFAULT_WAIT_TIME, LOGIN, PASSWORD
from locators import locators


@pytest.fixture(scope="session")  #
def browser():
    # driver = webdriver.Chrome(os.environ.get('CHROME_DRIVER_PATH'))
    driver = webdriver.Chrome('chromedriver.exe')  # put chromedriver folder path into PATH
    driver.implicitly_wait(DEFAULT_WAIT_TIME)
    driver.maximize_window()
    yield driver
    driver.quit()


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
    driver = browser  # get driver
    driver.get(browser.current_url)  # load current URL
    try:
        wait = WebDriverWait(driver, DEFAULT_WAIT_TIME)
        wait.until(EC.visibility_of_element_located(locators.SuitesPageLocators.HELLO_DPDN)).click()
        wait.until(EC.visibility_of_element_located(locators.SuitesPageLocators.LOGOUT_OPT)).click()
    except Exception as e:
        print("error occurred", e)
    finally:
        pass


@pytest.fixture(scope="function")
def close(browser):
    """ Delete cookies method for each test to skip logout"""
    yield close
    driver = browser  # get driver
    try:
        driver.delete_all_cookies()
    except Exception as e:
        print("error occurred", e)
    finally:
        pass


@pytest.fixture(params=['1qaz2wsx', '  45f  ',
                        'qqweqweqweqweqweqweqweqweqweqweqweqweqweqqqweqweqweqweqweqweqweqweqweqweqweqweqweqwe', LOGIN])
def parametrized_username(request):
    return request.param


@pytest.fixture(params=['', '  45_f', '#%123',
                        'Aa!@#$%^&*()-_+=`~,.?><|b  PaSSword!@#$%^&*()-_+=`~,.?><'])
def parametrized_password(request):
    return request.param


@pytest.fixture(params=['вав', '  33а_', 'ges_3445',
                        'f jfhd '])
def search_test_case(request):
    return request.param