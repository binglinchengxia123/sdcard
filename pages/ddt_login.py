import unittest
from selenium import webdriver
import ddt
from pages.login_page import DengLu


url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
testdata = [{"user": "admin", "psw": "123456", "expect": "admin"},
            {"user": "admin", "psw": "111111", "expect": "00"},
            {"user": "hhh", "psw": "123456", "expect": "222"}
            ]
@ddt.ddt
class Ddt_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.candao = DengLu(cls.driver)

    def setUp(self):
        self.driver.get(url)
        self.driver.delete_all_cookies()
        self.driver.refresh()

    # def login(self, user, psw, expect):
    #     self.candao.login(user)

    @ddt.data(*testdata)
    def test001(self, data):
        print("测试开始")
        print("测试数据%s" % data)
        self.candao.login(data["user"], data["psw"], data["expect"])
        print("测试结束")
        r = self.candao.get_user_name("admin")
        self.assertTrue(r)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

