from selenium import webdriver
#163登录
driver = webdriver.Firefox()

class NetEase():
    def __init__(self, driv):
        self.driv = driv


    def denglu(self):
        self.driv.get("https://mail.163.com/")
        #  打开浏览器，点击登录按钮，切换到登录界面
        self.driv.implicitly_wait(5)
        self.driv.switch_to.frame("x-URS-iframe")
        self.driv.find_element_by_name("email").send_keys("what568@163.com")
        self.driv.find_element_by_name("password").send_keys("suger123")
        self.driv.find_element_by_id("dologin").click()

    def getname(self):
        self.driv.implicitly_wait(10)
        self.driv.switch_to.default_content()

        try:
            s = self.driv.find_element_by_xpath(".//*[@id='spnUid']").text
            print(s)
            return s
        except:
            print("did not find!")

    # 进入写信页面方法
    def intowmail(self):
        self.driv.find_element_by_xpath(".//*[@id='_mail_component_69_69']/span[2]").click()
        driver.find_element_by_css_selector(".nui-editableAddr-ipt").send_keys("410086277@qq.com;")
        driver.find_element_by_xpath(".//*[@id='1534863187049_subjectInput']").send_keys("18651617372")




if __name__ == "__main__":

    login = NetEase(driv=driver)
    login.denglu()
    login.getname()
    login.intowmail()






