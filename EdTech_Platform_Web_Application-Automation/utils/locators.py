from selenium.webdriver.common.by import By

"""
Centralized Locator Repository to store all the locators class vice
"""

class HomePageLocators:
    signup_button =(By.XPATH,"//button[contains(text(),'Sign up')]")
    base_login_button = (By.XPATH,"//button[contains(text(),'Login')]")
    dobby=(By.ID,"zs_fl_chat")
    dobby_welcome = (By.XPATH,"//div[@class='textmsg-div']//child::span")
    signup_login = (By.XPATH,"//a[contains(text(),'Login')]")
       #menu
    LIVEClasses =(By.XPATH,"(//p[@class='⭐️f6lmuc-0 menu-hover text-sm font-medium text-nowrap leading-6'])[1]")
    Courses = (By.XPATH,"(//p[@class='⭐️f6lmuc-0 menu-hover text-sm font-medium text-nowrap leading-6'])[2]")
    Practice = (By.XPATH,"(//p[@class='⭐️f6lmuc-0 menu-hover text-sm font-medium text-nowrap leading-6'])[3]")
    Resources = (By.XPATH,"(//p[@class='⭐️f6lmuc-0 menu-hover text-sm font-medium text-nowrap leading-6'])[4]")
    Our_Products =(By.XPATH,"(//p[@class='⭐️f6lmuc-0 menu-hover text-sm font-medium text-nowrap leading-6'])[5]")

class LoginPageLocators:
    email=(By.XPATH,"//input[@id='email']")
    password=(By.XPATH,"//input[@id='password']")
    login = (By.ID,"login-btn"),
    invalid_feedback = (By.XPATH, "//div[@class='form-group']//div")


class DashboardPageLocators:
    profile_icon = (By.XPATH,"//div[@class='⭐️3hk5qd-0 gravatar-wrap']")
    logout=(By.XPATH,"//p[contains(text(),'Sign Out')]")


