import time
from selenium.webdriver.common.by import By
from datetime import datetime

class PagePIM:
    def __init__(self, driver):
        self.driver = driver

    #locator
    pim = "//span[contains(normalize-space(),'PIM')]"
    addCTA = "//button[normalize-space()='Add']"
    firstName = "//input[@placeholder='First Name']"
    lastName = "//input[@placeholder='Last Name']"
    saveCTA = "//button[normalize-space()='Save']"

    def click_PIM(self,fname,lname):
        time.sleep(4)
        self.driver.find_element(By.XPATH,self.pim).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.addCTA).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.firstName).send_keys(fname)
        self.driver.find_element(By.XPATH,self.lastName).send_keys(lname)
        self.driver.find_element(By.XPATH,self.saveCTA).click()