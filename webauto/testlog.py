from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"

driver = webdriver.Firefox()

driver.get(url)

def findElement(driver,locator,timout=5,t=1):


    ele1 = WebDriverWait(driver,timout,t).until(lambda x: x.find_element(*locator))
    return ele1

loc1 = (By.ID, "account")
loc2 = (By.NAME, "password")
loc3 = (By.ID, "submit")

findElement(driver,loc1).send_keys("admin")
findElement(driver,loc2).send_keys("123456")
findElement(driver,loc3).click()


# element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId"))

