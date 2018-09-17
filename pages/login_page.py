from selenium import webdriver
from common.base import Base

url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
class DengLu(Base):

    ys1 = ("xpath", ".//*[@id='account']")
    ys2 = ("name", "password")
    ys3 = ("xpath", ".//*[@id='submit']")

    ys4=("css selector","#myname")   #myname

    def login(self, user="admin", psw="123456", expect="admin"):
        self.driver.get(url)
        self.sendkeys(self.ys1, user)
        self.sendkeys(self.ys2, psw)
        self.click(self.ys3)
        self.is_text_in_element(self.ys4, expect)

    def get_title_name(self, title):
        self.is_title(title)

    def get_user_name(self, expect):
        p = self.is_text_in_element(self.ys4, expect)
        return p



if __name__ == "__main__":
    driver = webdriver.Firefox()
    chandao = DengLu(driver)
    chandao.login()
    o = chandao.is_title("我的地盘 - 禅道")
    print(o)
    po = chandao.get_user_name("admin")
    print(po)






