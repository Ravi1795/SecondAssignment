from selenium.webdriver.common.by import By
import datetime
import os
import time


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    # locators
    admin = "//span[text()='Admin']"
    systemuser = "(//input[@class='oxd-input oxd-input--active'])[2]"
    searchbtn = "//button[@type='submit']"
    resetbtn = "//button[@class='oxd-button oxd-button--medium oxd-button--ghost']"
    msg = "//div[text()='FMLName']"

    def Admin(self):
        self.driver.find_element(By.XPATH, self.admin).click()

    def enterSystemUser(self, user):
        self.driver.find_element(By.XPATH, self.systemuser).send_keys(user)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.searchbtn).click()

    def resetsearch(self):
        self.driver.find_element(By.XPATH, self.resetbtn).click()

    def verifySuccessfulSearch(self):
        element = self.driver.find_element(By.XPATH, self.msg)
        txtelement = element.text
        if element is not None:
            print(f"Searched User {txtelement}")
            return True
        else:
            return False

    def invalidSearch(self, user1=""):
        time.sleep(2)
        self.resetsearch()
        self.Admin()
        self.enterSystemUser(user1)
        time.sleep(2)
        self.clickSearch()

    def userSearch(self, user=""):
        time.sleep(2)
        self.Admin()
        self.enterSystemUser(user)
        time.sleep(2)
        self.clickSearch()

