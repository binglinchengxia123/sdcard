from selenium import webdriver
from common.base import Base
import time

class AddProduct(Base):
    ys14 = ("xpath", ".//*[@id='mainmenu']/ul/li[2]/a")  # 产品按钮  click
    ys15 = ("xpath", ".//*[@id='modulemenu']/ul/li[11]/a")  # 添加产品按钮 click
    ys16 = ("xpath", ".//*[@id='name']")  # 输入产品名称 sendkeys
    ys17 = ("xpath", ".//*[@id='code']")  # 输入产品编号 sendkeys
    ys18 = ("xpath", ".//*[@id='QD_chosen']/a")  # 点击测试负责人框 click
    ys19 = ("xpath", ".//*[@id='QD_chosen']/div/ul/li")  # 选择测试负责人 admin  click
    ys20 = ("xpath", ".//*[@id='submit']")  # 保存按钮  click
    ys21 = ("xpath", ".//*[@id='treebox']/div/div/div[1]/strong")  # 定位的新建的产品名称
    ys13 = ("class name", "article-content")

    def add_product(self, title):
        self.click(self.ys14)
        self.click(self.ys15)
        self.sendkeys(self.ys16, title)
        timestr = time.strftime("%Y%m%d%H%M%S")
        code = "6303"
        self.sendkeys(self.ys17, code+timestr)
        self.click(self.ys18)
        self.click(self.ys19)
        frame = self.findElement(("class name", "ke-edit-iframe"))
        self.driver.switch_to.frame(frame)
        body = "如果超人会飞"
        self.sendkeys(self.ys13, body)
        self.driver.switch_to.default_content()
        self.click(self.ys20)

    def is_add_product_ok(self, text_):
        return self.is_text_in_element(self.ys21, text_)