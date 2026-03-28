#dashboradpage
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM.BasePage import BasePage
from POM.LoginPage import LoginPage
from utils.config import TIMEOUT
from utils.locators import DashboardPageLocators as DL
from utils.locators import HomePageLocators as HL


class DashboardPage(LoginPage, BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)#explicit wait
#logout function
    def logout(self):
        try:
            self.wait.until(EC.element_to_be_clickable(DL.profile_icon)).click() #ensures profile is clicked
            self.wait.until(EC.element_to_be_clickable(DL.logout)).click() #explicitly wait for logout to be clicked
            self.wait.until(EC.url_changes(*self.driver.current_url)) #waitsfor page to be redirected
            return True
        except Exception as e:
            print(f"Logout failed: {e}")
            return False

# Validates the logout by checking URL.
    def is_logged_out(self):
            try:
                self.wait.until(EC.url_to_be("https://www.guvi.in/"))
                # Optional DOM check for login button
                return self.wait.until(EC.presence_of_element_located(HL.base_login_button)).is_displayed()
            except TimeoutException:
                print(f"Post-logout URL mismatch: {self.driver.current_url}")
                return False


