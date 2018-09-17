#  expected_conditions 仿函数用法

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from common.base import Base

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")
zen = Base(driver)
# a = EC.title_is("百度一下，你就知道")(driver) #传两个参数，一个是期望的title，一个是实际的title
# a = zen.is_title("百度一下，你就知道")
# print(a)
# lo2 = ("xpath", ".//*[@id='lh']/a[4]")
# b = EC.text_to_be_present_in_element(lo2,"百度推广")(driver)

m1 = zen.is_title("百度一下，你就知道")
print(m1)
# m2 = zen.is_title_contains("知道")
# print(m2)
# lo2 = ("xpath", ".//*[@id='lh']/a[4]")
# m3 = zen.is_text_in_element(lo2,"百度")
# print(m3)