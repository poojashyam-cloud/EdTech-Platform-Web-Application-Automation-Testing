from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.BasePage import BasePage
from utils.config import TIMEOUT
from utils.locators import LoginPageLocators as LL

class LoginPage(BasePage):

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def enter_email(self, username):
        self.enter_text(LL.email, username)

    def enter_password(self, password):
        self.enter_text(LL.password, password)

    def click_login(self):
        login_btn = self.driver.find_element(By.ID,"login-btn")
        login_btn.click()

    def get_error_message(self):
        return self.driver.find_element(LL.invalid_feedback).text


    def failed_login(self):
        try:
            error_element = WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(LL.invalid_feedback))
            assert error_element.is_displayed(), "Error message not displayed"  # Raises assertion if error message is missing
            print(f"Login failed as expected. Message: {error_element.text}")
        except Exception as e:
            # Screenshot on failure
            raise AssertionError("Login did not fail as expected or error message missing") from e
