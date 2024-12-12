import os
import time
from selenium.webdriver.common.by import By
from datetime import datetime

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # locators

    username = "//input[@name='username']"
    password = "//input[@name='password']"
    loginCTA = "//button[@type='submit']"

    def enterUsername(self, username):
        self.driver.find_element(By.XPATH, self.username).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.password).send_keys(password)

    def clickCTA(self):
        self.driver.find_element(By.XPATH, self.loginCTA).click()

    def login(self, username="", password=""):
        time.sleep(2)
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickCTA()
        time.sleep(5)
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        screenshot_name = os.path.join("C:\\Users\\ravi.yadav_infobeans\\PycharmProjects\\SecondAssignment\\screenshots",
                                       f"screenshot_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")