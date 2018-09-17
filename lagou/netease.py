from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://study.163.com/")

driver.implicitly_wait(10)

driver.find_element_by_xpath(".//*[@id='ux-modal']/div[1]/a/i").click()

driver.find_element_by_xpath(".//*[@id='auto-id-1534611526113']").click()

driver.implicitly_wait(5)
# driver.find_element_by_xpath(".//*[@id='auto-id-1534609974403']").click()
#
# driver.switch_to.frame("x-URS-iframe1534610420267.386")
#
# driver.find_element_by_name("email").send_keys("what568@163.com")
# driver.find_element_by_name("password").send_keys("suger123")
# driver.find_element_by_id("dologin").click()


#x-URS-iframe1534610420267.386

#driver.find_element_by_id("auto-id-1534609238901").click()



#x-URS-iframe1534609240912.1384