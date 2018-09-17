import unittest
from pages.login_page import DengLu
from selenium import webdriver

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.zentao = DengLu(cls.driver)
        cls.driver.get("http://127.0.0.1/zentao/user-login.html")

    def test001(self):
        self.zentao.login()

    def test002(self):
        k = self.zentao.is_title("我的地盘 - 禅道")
        self.assertTrue(k)

if __name__ == "__main__":
    unittest.main()


