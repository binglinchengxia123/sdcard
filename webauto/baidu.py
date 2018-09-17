from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox()

driver.get("https://www.baidu.com/")
mouse = driver.find_element_by_xpath(".//*[@id='u1']/a[8]")  #定位到设置按钮
ActionChains(driver).move_to_element(mouse).perform() # 鼠标移动到设置按钮
driver.find_element_by_xpath(".//*[@id='wrapper']/div[6]/a[1]").click()
time.sleep(2)

s = driver.find_element_by_id("nr")  #定位到设置搜索条数
Select(s).select_by_index(1)  # 这是根据index选择
# Select(s).select_by_value("20")  # 这是根据value值选择
s.click()
# driver.find_element_by_id("nr").click()
# time.sleep(1)
# driver.find_element_by_xpath(".//*[@id='nr']/option[3]").click()
driver.find_element_by_xpath(".//*[@id='gxszButton']/a[1]").click()
time.sleep(3)
a = driver.switch_to.alert
def is_alert_exist():
    try:
        # a = driver.switch_to.alert #切换到alter弹框
        return True
    except:
        return False

if is_alert_exist():

    print(a.text)
else:
     pass



