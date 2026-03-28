from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.BasePage import BasePage
from utils.config import TIMEOUT
from utils.locators import HomePageLocators as HL

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_base_login_button_visible(self):
        try:
            self.is_element_visible(HL.base_login_button)
            return True
        except Exception as e:
            print(e)
            return False

    def is_base_login_button_clickable(self):
        try:
            element = WebDriverWait(self.driver,TIMEOUT).until(EC.element_to_be_clickable(HL.base_login_button))
            return element.is_displayed() and element.is_enabled()
        except Exception as e:
            print(f"Login button not clickable: {e}")
            return False

    def click_base_login_btn(self):
        try:
            self.click(HL.base_login_button)
            return True
        except Exception as e:
            print(f"Login button not clickable: {e}")
            return False

    def is_sign_in_btn_visible(self):
        return  self.is_element_visible(HL.signup_button).is_displayed()

    def is_sign_in_btn_clickable(self):
        try:
            self.is_element_clickable(HL.signup_button).is_enabled()
            return True
        except Exception as e:
            print(f"Signin button not clickable: {e}")
            return False

    def click_signup_btn(self):
        try:
            self.click(HL.signup_button)
            return True
        except Exception as e:
            print(f"Signup button not clicked: {e}")
            return False

    def navigate_to_login_from_signup_page(self):
        self.click(HL.signup_button)
        self.click(HL.signup_login)

    def check_menu_items_visible(self):
        return {self.is_element_visible(HL.Courses) and
            self.is_element_visible(HL.LIVEClasses) and
            self.is_element_visible(HL.Practice) }

    def check_menu_items_clickable(self):
        try:
            self.is_element_clickable(HL.Courses)
            self.is_element_clickable(HL.LIVEClasses)
            self.is_element_clickable(HL.Practice)
            return True
        except Exception as e:
            print(f"Menu items not visible: {e}")
            return False

    def dobby_chatbot(self):
        elem = WebDriverWait(self.driver,TIMEOUT).until(presence_of_element_located(HL.dobby))
        return elem.is_displayed()

    def is_dobby_welcome_visible(self):
        try:
            element = self.driver.find_element(HL.dobby_welcome)
            return element.is_displayed()
        except Exception as e:
            print(f"Dobby welcome message not found: {e}")
            return False