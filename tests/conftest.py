import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import SuitesPageLocators
from utils.constants import DEFAULT_WAIT_TIME


@pytest.fixture(scope="session")  #
def browser():
    # driver = webdriver.Chrome(os.environ.get('CHROME_DRIVER_PATH'))
    driver = webdriver.Chrome('chromedriver.exe')  # put chromedriver folder path into PATH
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    current_url = driver.current_url
    driver.get(current_url)
    try:
        wait = WebDriverWait(driver, DEFAULT_WAIT_TIME)
        hello_user = wait.until(EC.visibility_of_element_located(SuitesPageLocators.HELLO_DPDN))
        hello_user.click()
        logout_click = wait.until(EC.visibility_of_element_located(SuitesPageLocators.LOGOUT_OPT))
        logout_click.click()
    except Exception as e:
        print("error occurred", e)
    finally:
        pass
    driver.quit()


@pytest.fixture(scope="function")
def logout(browser):
    """ Logout method for each test
        'Hello,User' options-> 'Logout' will be executed in test's last page"""
    yield logout
    driver = browser  # get driver
    driver.get(browser.current_url)  # load current URL
    try:
        wait = WebDriverWait(driver, DEFAULT_WAIT_TIME)
        hello_user = wait.until(EC.visibility_of_element_located((By.ID, "navbarDropdownMenuLink")))
        hello_user.click()
        logout_click = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/logout']")))
        logout_click.click()
    except Exception as e:
        print("error occurred", e)
    finally:
        pass

