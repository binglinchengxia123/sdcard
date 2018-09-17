from webauto.mailbox import NetEase
from selenium import webdriver
import time
import unittest

class NetEaseLogIn(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.mailbo = NetEase(cls.driver)

    def setUp(self):
        self.driver.get("http://mail.163.com/js6/main.jsp?sid=xCTTnxjVxXkMEwIjtTVVucpeHYwgwhuB&df=unknow#module=mbox.ListModule%7C%7B%22fid%22%3A1%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%7D")
        self.driver.delete_all_cookies()  # 清空cookies
        self.driver.refresh()

    def test_01(self):
        ''' 调用登录函数进行登录 '''
        self.mailbo.denglu()
        time.sleep(3)
        x = self.mailbo.getname()
        print("用户名是%s"%x)     #打印出获取到的用户名
        self.assertTrue(x == "what568@163.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()



