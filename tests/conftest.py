import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path=r"D:/webdrivers/chromedriver_win32/chromedriver.exe")
    yield driver
    driver.quit()
