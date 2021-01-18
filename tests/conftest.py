import os
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    #driver = webdriver.Chrome(os.environ.get('CHROME_DRIVER_PATH'))
    driver = webdriver.Chrome('chromedriver.exe')  # put chromedriver folder path into PATH
    yield driver
    driver.quit()
