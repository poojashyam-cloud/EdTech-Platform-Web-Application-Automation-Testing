import time
from selenium.webdriver.support.ui import WebDriverWait as wait
import pytest
from POM.HomePage import BasePage, HomePage
from POM.DasboardPage import DashboardPage
from POM.LoginPage import LoginPage
from utils.config import TIMEOUT
from utils.dataloader import load_test_data
from utils.locators import DashboardPageLocators as DL
from selenium.webdriver.support import expected_conditions as EC
import logging

#loads test data from json and temporarily stores in a variable td
td = load_test_data("C:\\Users\\HP\\PycharmProjects\\EdTech_Platform_Web_Application-Automation\\Test_data\\testdata.json")

def test_title_validation(driver):
    logging.info("--Test 1 Title validation started--")
    bp = BasePage(driver)
    try:
        assert bp.get_title() == "HCL GUVI | Learn to code in your native language","title mismatch"
        driver.save_screenshot("title_validation_passed.png")
        logging.info("--Test passed--")
    except AssertionError:
        logging.error("--title mismatch,--Test Failed--")
        driver.save_screenshot("tc1mismatch_error.png")
        raise

def test_validate_url(driver):
    logging.info("--Test 2 URL validation started--")
    BasePage(driver)
    try:
        assert "guvi" in driver.current_url,"url mismatch"
        driver.save_screenshot("URL_validation_passed.png")
        logging.info("--Test passed")
    except AssertionError:
        logging.error("--url mismatch,--Test Failed")
        driver.save_screenshot("URL_validation_error.png")


def test_is_login_button_visible(driver):
    logging.info("--Test 3 Login button validation started--")
    hp = HomePage(driver)
    try:
        assert hp.is_base_login_button_visible(),"login button not visible"
        driver.save_screenshot("is_login_button_visible.png")
        logging.info("--Test passed--")#validating is visible
    except AssertionError:
        logging.error("login button not visible,--Test Failed--")
        driver.save_screenshot("is_login_button_error.png")

def test_is_signup_button_visible(driver):
    logging.info("--Test 4 signup button validation started--")
    hp = HomePage(driver)
    try:
        assert hp.is_sign_in_btn_visible(), "signup button not visible"  # validating is visible
        driver.save_screenshot("is_signup_button_visible.png")
        logging.info("--Test passed--")  # validating is visible
    except AssertionError:
        logging.error("signup button not visible,--Test Failed--")
        driver.save_screenshot("is_signup_button_error.png")

def test_navigate_to_login_page_from_signup_page(driver):
    logging.info("--Test 4 Navigate to login page from signup page--")
    hp = HomePage(driver)
    hp.navigate_to_login_from_signup_page()
    time.sleep(5)
    expected_url = "https://www.guvi.in/sign-in/"
    assert expected_url in driver.current_url,"not redirected to login page from signup page"

def test_verify_login_function_valid(driver):
    hp = HomePage(driver)
    hp.click_base_login_btn()
    lp = LoginPage(driver)
    driver.execute_script("window.scrollBy(0, 500);")
    email =td["valid_login"]["email"]
    password = td["valid_login"]["password"]
    lp.login(email,password)
    icon = wait(driver,TIMEOUT).until(EC.presence_of_element_located(DL.profile_icon))
    assert icon.is_displayed(),"User did not login" #conforming user logged in with presence of profile icon


def test_verify_login_function_invalid(driver):
    hp = HomePage(driver)
    hp.click_base_login_btn()
    lp = LoginPage(driver)
    email = td["invalid_login"]["email"]
    password = td["invalid_login"]["password"]
    lp.login(email,password)
    lp.failed_login()


def test_menu_items_display(driver):  # Assumes a fixture is injecting the WebDriver instance
    hp = HomePage(driver)
   # assert hp.check_menu_items_clickable(), "Menu items are not clickable"
    assert hp.check_menu_items_visible(), "Menu items are not visible"

def test_dobby_chatbot(driver):
    hp = HomePage(driver)
    assert hp.dobby_chatbot(), "dobby chatbot not visible"

def test_logout_function_flow(driver):
    hp = HomePage(driver)
    hp.click_base_login_btn()
    lp = LoginPage(driver)
    email = td["valid_login"]["email"]
    password = td["valid_login"]["password"]
    lp.login(email,password)
    db = DashboardPage(driver)
    db.logout()
    expected_logout_url = "https://www.guvi.in/"
    actual_url = driver.current_url
    assert actual_url == expected_logout_url, f"Expected logout URL: {expected_logout_url}, but got: {actual_url}"
    # Validates URL after proper logout and navigate to the base page








