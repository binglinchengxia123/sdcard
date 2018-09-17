
from selenium import webdriver
from common.base import Base
import time
# import requests

class ChanDao(Base):


    # 登录
    ys1 = ("xpath", ".//*[@id='account']")
    ys2 = ("name", "password")
    ys3 = ("xpath", ".//*[@id='submit']")
    #  添加bug
    ys4 = ("xpath", ".//*[@id='mainmenu']/ul/li[4]/a") #click
    ys5 = ("xpath", ".//*[@id='modulemenu']/ul/li[2]/a") #click
    ys6 = ("xpath", ".//*[@id='createActionMenu']/a")  #click
    ys7 = ("xpath", ".//*[@id='openedBuild_chosen']/ul")  #click
    ys8 = ("xpath", ".//*[@id='openedBuild_chosen']/div/ul/li") #click
    ys9 = ("xpath", ".//*[@id='title']")  #这个是sendkeys
    ys13 = ("class name", "article-content")
    ys10 = ("xpath", "操作步骤")  # 这个要先swith to iframe, 然后这边直接sendkeys
    ys11 = ("xpath", ".//*[@id='submit']")  #click
    ys12 = ("xpath", ".//*[@id='bugList']/tbody/tr/td[4]/a")  #这个是bug列表的第一个bug标题
    ys14 = ("xpath", ".//*[@id='mainmenu']/ul/li[2]/a") # 产品按钮  click
    ys15 = ("xpath", ".//*[@id='modulemenu']/ul/li[11]/a") #添加产品按钮 click
    ys16 = ("xpath", ".//*[@id='name']")  # 输入产品名称 sendkeys
    ys17 = ("xpath", ".//*[@id='code']")  # 输入产品编号 sendkeys
    ys18 = ("xpath", ".//*[@id='QD_chosen']/a") #点击测试负责人框 click
    ys19 = ("xpath", ".//*[@id='QD_chosen']/div/ul/li")# 选择测试负责人 admin  click
    ys20 = ("xpath", ".//*[@id='submit']") #保存按钮  click
    ys21 = ("xpath", ".//*[@id='treebox']/div/div/div[1]/strong") #定位的新建的产品名称


    def login(self, user="admin", psw="123456"):

        self.driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
        self.sendkeys(self.ys1, user)
        self.sendkeys(self.ys2, psw)
        self.click(self.ys3)


    # def add_bug(self, title):
    #     self.click(self.ys4)
    #     time.sleep(2)
    #     self.click(self.ys5)
    #     time.sleep(2)
    #     self.click(self.ys6)
    #     time.sleep(2)
    #     self.click(self.ys7)
    #     time.sleep(2)
    #     self.click(self.ys8)
    #     # timestr = time.strftime("%Y%m%d%H%M%S")
    #     self.sendkeys(self.ys9, title)
    #     # 输入操作步骤
    #     frame = self.findElement(("class name", "ke-edit-iframe"))
    #     self.driver.switch_to.frame(frame)
    #     body = "where did you go"
    #     self.sendkeys(self.ys13, body)
    #     self.driver.switch_to.default_content()
    #     self.click(self.ys11)
    #
    # def is_add_bug_success(self,text_):
    #     return self.is_text_in_element(self.ys12,text_)
    #
    # def add_product(self, title):
    #     self.click(self.ys14)
    #     self.click(self.ys15)
    #     self.sendkeys(self.ys16, title)
    #     timestr = time.strftime("%Y%m%d%H%M%S")
    #     code = "6303"
    #     self.sendkeys(self.ys17, code+timestr)
    #     self.click(self.ys18)
    #     self.click(self.ys19)
    #     frame = self.findElement(("class name", "ke-edit-iframe"))
    #     self.driver.switch_to.frame(frame)
    #     body = "如果超人会飞"
    #     self.sendkeys(self.ys13, body)
    #     self.driver.switch_to.default_content()
    #     self.click(self.ys20)
    #
    # def is_add_product_ok(self, text_):
    #     return self.is_text_in_element(self.ys21, text_)

if __name__ == "__main__":
    driver = webdriver.Firefox()

    zentao = ChanDao(driver)
    zentao.login()

    # timestr = time.strftime("%Y%m%d%H%M%S")
    # title = "我提交的bug"+timestr
    # zentao.add_bug(title)
    # result = zentao.is_add_bug_success(title)
    #print(result)
    # title = "止战之殇"
    # zentao.add_product(title)
    # result = zentao.is_add_product_ok(title)
    # print(result)



