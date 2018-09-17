from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Base():

    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5
    # 定位到返回元素，没定位到返回timeout超时

    def findelementNew(self, locator):
        '''定位到元素，返回元素对象，没定位到返回timeout异常'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0],locator[1]))
            ele1 = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return ele1

    def findElement(self, locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))
            ele1 = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele1

    def findElements(self,locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
        else:
            try:
                print("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))
                ele1 = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
                return ele1
            except:
                return []


    def sendkeys(self, locator, text):
        '''send_keys方法封装'''

        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator):

        ele = self.findElement(locator)
        ele.click()

    def clear(self):

        self.clear()

    def is_title(self, title):
        try:
            '''判断返回的title和要获取的页面title是否一致，结果是布尔值'''
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    def is_title_contains(self, text):
        try:
            '''判断返回的title文本是否包含预期的文本值，结果是布尔值'''
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(text))
            return result
        except:
            return False

    def is_text_in_element(self, locator, text_):
        '''判断返回的title是否在定位的元素中 ，结果是布尔值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, text_))
            return result
        except:
            return False

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False






    









if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
    zentao = Base(driver)
    loc1 = (By.ID, "account")
    loc2 = (By.NAME, "password")
    loc3 = (By.ID, "submit")
    zentao.sendkeys(loc1, "admin")
    zentao.sendkeys(loc2, "123456")
    zentao.click(loc3)

