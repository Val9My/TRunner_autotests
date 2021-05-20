from selenium.webdriver.support.expected_conditions import staleness_of
from urllib.parse import urlparse
from utils.constants import DEFAULT_WAIT_TIME
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import BasePageLocators
import time
from selenium.webdriver.common.action_chains import ActionChains


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        self.browser.get(url)

    def get_title(self):
        title = self.browser.title
        print(time.strftime("%Y-%m-%d | %H:%M:%S ") + "Page title = " + str(title))
        return title

    def find_element(self, locator):
        """Method to find visible element"""
        try:
            wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
            element = wait.until(EC.element_to_be_clickable(locator))
            # element = wait.until(EC.visibility_of_element_located(element))
            return element
        except TimeoutException:
            print(f"Locator {locator} not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print(f"Locator {locator} in 'find_element' - An Exception occurred:", e)

    def find_elements(self, locators):
        """Method to find visible element"""
        try:
            wait = WebDriverWait(self.browser, DEFAULT_WAIT_TIME)
            elements = wait.until(EC.presence_of_all_elements_located(locators))
            return elements
        except TimeoutException:
            print(f"Locators {locators} not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print(f"Locators {locators} in 'find_elements' - An Exception occurred:", e)

    def visible_element_click(self, locator, n=0):
        """ Method to click on element or 'nth' element from list of elements when it get visible"""
        try:
            element = self.find_elements(locator)
            element[n].click()
        except Exception as e:
            print(f"Locator {locator} in 'visible_element_click' - An Exception occurred:", e)

    def visible_element_mb3_click(self, locator, n=0):
        """ Method to click MB3 on element or 'nth' element from list of elements when it get visible"""
        try:
            chain = ActionChains(self.browser)
            element = self.find_elements(locator)
            chain.context_click(element[n]).perform()
        except Exception as e:
            print(f"Locator {locator} in 'visible_element_mb3_click' - An Exception occurred:", e)

    def visible_element_double_click(self, locator, n=0):
        """ Method to click MB3 on element or 'nth' element from list of elements when it get visible"""
        try:
            chain = ActionChains(self.browser)
            element = self.find_elements(locator)
            chain.double_click(element[n]).perform()
        except Exception as e:
            print(f"Locator {locator} in 'visible_element_double_click' - An Exception occurred:", e)

    def visible_element_send_text(self, locator, text, n=0):
        """ Method to input text in element or 'nth' element from list of elements when it get visible"""
        try:
            elements = self.find_elements(locator)
            elements[n].send_keys(text)
        except Exception as e:
            print(f"Locator {locator} in 'visible_element_send_text' - An Exception occurred:", e)

    def visible_element_get_text(self, locator, n=0):
        """ Method to get 'text' from element or 'nth' element from list of elements when it get visible"""
        try:
            element = self.find_elements(locator)
            print("Get Text =", element[n].text)
            return element[n].text
        except Exception as e:
            print(f"Locator {locator} in 'visible_element_get_text' - An Exception occurred:", e)

    def visible_element_clear_text(self, locator, n=0):
        """ Method to delete text from textbox or 'ntx' textbox in list of elements when it get visible"""
        try:
            element = self.find_elements(locator)
            element[n].clear()
        except Exception as e:
            print(f"Locator {locator} in 'visible_element_click' - An Exception occurred:", e)

    def visible_element_get_value(self, locator, n=0):
        """ Method to get 'value' from element or 'ntx' element in list of elements when it get visible"""
        try:
            element = self.find_elements(locator)
            print('Get Value =', element[n].get_attribute('value'))
            return element[n].get_attribute('value')
        except Exception as e:
            print(f"Locator {locator} in 'visible_element_get_value' - An Exception occurred:", e)

    def visible_element_get_class(self, locator, n=0):
        """ Method to get 'class' value from element or 'ntx' element in list of elements when it get visible"""
        try:
            element = self.find_elements(locator)
            print("Get Class =", element[n].get_attribute('class'))
            return element[n].get_attribute('class')
        except Exception as e:
            print(f"Locator {locator} in 'visible_element_get_class' - An Exception occurred:", e)

    def trunner_lnk_click(self):
        """ Click on 'TRunner' link"""
        self.visible_element_click(BasePageLocators.TRUNNER_LNK)

    def test_suites_lnk_click(self):
        """ Click on 'Test Suites' link """
        self.visible_element_click(BasePageLocators.TEST_SUITES_LNK)

    def suite_manager_lnk_click(self):
        """ Click on 'Suite Manager' link """
        self.visible_element_click(BasePageLocators.SUITE_MANAGER_LNK)

    def about_lnk_click(self):
        """ Click on 'About' link """
        self.visible_element_click(BasePageLocators.ABOUT_LNK)

    def hello_user_click(self):
        """ Click on 'Hello, User' drop-down """
        self.visible_element_click(BasePageLocators.HELLO_USER_DPDN)

    def user_settings_select(self):
        """ Click on 'Hello, User -> Settings' drop-down """
        self.visible_element_click(BasePageLocators.SETTINGS_OPT)

    def user_logout_select(self):
        """ Click on 'Hello, User -> Logout' drop-down """
        self.visible_element_click(BasePageLocators.LOGOUT_OPT)

    def get_user_name_from_hello(self):
        """ Get username in 'Hello, user' dropdown """
        try:
            user = self.find_element(BasePageLocators.HELLO_USER_DPDN).text.partition(' ')[2]
            return user
        except Exception as e:
            print(" In 'get_user_name_from_hello' - An Exception occurred:", e)

    def get_text_from_alert(self):
        """Getting text from alert dialog"""
        try:
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            return alert_text
        except TimeoutException:
            print(f" 'Alert' window not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print(" In 'get_text_from_alert' - An Exception occurred:", e)

    def handling_alert(self):
        """Alert acceptation"""
        try:
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert.accept()
        except TimeoutException:
            print(f" 'Alert' window not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print(" In 'handling_alert' - An Exception occurred:", e)

    def is_element_seen(self, locator, n=0):
        """ Check that element seen on page """
        try:
            element = self.find_elements(locator)
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.visibility_of(element[n]))
            return True
        except TimeoutException as e:
            print(locator, " - element is not seen timeout error", e)
            return False

    def are_elements_seen(self, locators):
        """ Check that all elements from list of elements seen on page """
        try:
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.visibility_of_all_elements_located(locators))
            return True
        except TimeoutException as e:
            print(locators, " - elements are not seen timeout error", e)
            return False

    def wait_new_page_load(self):
        """ Check that current page URL changes to new """
        #curr_url = self.browser.find_element_by_tag_name('html')
        curr_url = self.browser.current_url  # get current URL
        try:
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(staleness_of(curr_url))  # (EC.url_changes(curr_url))
        #except Exception as e:
            #print(" Just loading new page:", e)
        except AttributeError:
            #print(" Just loading new page.....")
            pass
        finally:
            pass
        self.browser.get(self.browser.current_url)  # set new URL

    def input_text_in_field(self, locator, text):
        """Input some text in fields"""
        tbx = WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(
                EC.element_to_be_clickable(locator))
        tbx.send_keys(text, Keys.RETURN)

    def click_several_buttons(self, locators):
        """Click several buttons one by one"""
        buttons = None
        try:
            buttons = self.find_elements(locators)
            #print("Buttons count= ", len(buttons))
            for button in buttons:
                button.click()
        except TimeoutException:
            print(f"Buttons {buttons} not found after {DEFAULT_WAIT_TIME} seconds")
        except Exception as e:
            print(f"Buttons {buttons} in 'click_several_buttons' - An Exception occurred:", e)

    def forward(self):
        """To move forward in browser history"""
        self.browser.forward()

    def backward(self):
        """To move backward in browser history"""
        self.browser.back()

    def get_element_location(self, locator):
        """Method for getting element location on WebPage"""
        try:
            element = self.find_element(locator)
            return element.location
        except Exception as e:
            print(f"Locator {locator} in 'get_element_location' - An Exception occurred:", e)

    def get_element_size(self, locator):
        """Method for getting element size on WebPage"""
        try:
            element = self.find_element(locator)
            return element.size
        except Exception as e:
            print(f"Locator {locator} in 'get_element_size' - An Exception occurred:", e)

    def get_css_property(self, locator, css_property):
        """Method for getting css styles of WebElement"""
        element = self.find_element(locator)
        element_property = element.value_of_css_property(css_property)
        return element_property

    def move_mouse_on_element(self, locator, n=0):
        """Method to move mouse on element or 'nth' element in list of elements"""
        action = ActionChains(self.browser)
        element = self.find_elements(locator)  # or your another selector here
        action.move_to_element(element[n])
        action.perform()

    def move_mouse_by_offset(self, locator, x, y):
        """Method to move mouse by offset (x-to the right, y to the bottom) """
        action = ActionChains(self.browser)
        element = self.find_element(locator)
        action.move_to_element(element)
        action.perform()
        action.move_by_offset(x, y)
        action.perform()

    def extract_domain_from_url(self, url):
        """Methods that allows extract domain name from url"""
        domain = urlparse(url).netloc
        return domain