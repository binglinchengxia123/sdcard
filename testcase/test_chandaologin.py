from selenium import webdriver
from webauto.chandao import ZenTao
import unittest
import time
#
class ChanDao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.candao = ZenTao(cls.driver)

    def setUp(self):
        self.driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test01(self):
        self.candao.chandaologin()
        time.sleep(3)
        y = self.candao.is_login_ok()
        print("用户名是%s" % y)
        self.assertTrue(y == "退出")

    def test_02(self):
        '''登录成功的案例'''
        time.sleep(2)
        self.candao.chandaologin()
        # 判断是否登陆成功
        time.sleep(3)
        t = self.get_login_username()
        print("获取的结果：%s" % t)
        self.assertTrue(t == "admin")

    def test_03(self):
        '''登录失败的案例'''
        time.sleep(2)
        # 错误账号和密码
        self.login("admin1", "")
        # 判断是否登陆成功
        time.sleep(3)
        t = self.get_login_username()
        print("登录失败，获取结果：%s" % t)
        self.assertTrue(1 == 2)  # 断言失败截图
        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
