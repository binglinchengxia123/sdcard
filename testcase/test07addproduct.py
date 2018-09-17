import unittest
from selenium import webdriver
from pages.add_product_page import AddProduct
from pages.login_page import DengLu

class NewProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.nwepro = AddProduct(cls.driver)
        cls.driver.get("http://127.0.0.1/zentao/user-login.html")
        cls.log = DengLu(cls.driver)

    def setUp(self):
        self.log.login()

    def test001(self):
        title = "仙人掌是好吃的吗"
        self.nwepro.add_product(title)
        r = self.nwepro.is_add_product_ok(title)
        self.assertTrue(r)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()