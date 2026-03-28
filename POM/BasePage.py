import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import TIMEOUT

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,TIMEOUT)

    def click(self, locator):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title

    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def take_screenshot(self, name="screenshot"):
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)

        file_name = f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        path = os.path.join(folder, file_name)

        self.driver.save_screenshot(path)
        return path
