from selenium import webdriver
import time

class ZenTao():
    def __init__(self, ace):
        self.driver = ace # ace只是一个形参 可以随便起名字，对应代码下方的ace = webdriver.Firefox()

    def chandaologin(self):
        self.driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_id("submit").click()
        time.sleep(3)

    def is_login_ok(self):
        try:
            a = self.driver.find_element_by_xpath(".//*[@id='topnav']/a[1]").text
            print(a)
            return a
        except:
            print("没有找到退出按钮")


if __name__ == "__main__":
    ace = webdriver.Firefox()
    login = ZenTao(ace)
    login.chandaologin()
    login.is_login_ok()
