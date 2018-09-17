import unittest
from selenium import webdriver
from testcase.dengluzt import ChanDao
import time
class TestAddBug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.zentao = ChanDao(cls.driver)
        cls.driver.get("http://127.0.0.1/zentao/user-login.html")
        cls.zentao.login()

    def setUp(self):

        self.zentao.driver.get("http://127.0.0.1/zentao/my/")

    def test_add_bug(self):
        timestr = time.strftime("%Y%m%d%H%M%S")
        title = "我提交的bug"+timestr
        self.zentao.add_bug(title)
        result = self.zentao.is_add_bug_success(title)
        self.assertTrue(result)

    def test_add_product(self):
        title = "止战之殇1"
        self.zentao.add_product(title)
        result = self.zentao.is_add_product_ok(title)
        print(result)


if __name__ == "__main__":
    unittest.main()