# coding:utf-8
import requests
import urllib3
from bs4 import BeautifulSoup
import re
import unittest

urllib3.disable_warnings()


class LaGouWang():
    def __init__(self, s):
        self.s = s

    def gettoken(self):
        '''s是形参，这个函数是为了获取登录的token，s用来传 s = requests.session()
        h是请求头部，必须带的参数，不带会被认为是脚本访问
        return 要返回 {"Anti_Forge_Token":"xxx","Anti_Forge_Code":"xxx"}
        '''
        url = "https://passport.lagou.com/login/login.html"

        h = {

            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
        r = self.s.get(url, headers=h, verify=False)

        # print(r.text)
        # from_encoding='utf-8'
        soup = BeautifulSoup(r.content, "html.parser")
        t = soup.find_all("script")[1].get_text()
        # print(t)
        tok = {}  # 定义一个字典，用来放下面两个动态参数
        try:
            Anti_Forge_Token = re.findall("Forge_Token = \'(.+?)\'", t)  # 正则表达式提取出对应的值
            # print(Anti_Forge_Token[0])
            tok["Anti_Forge_Token"] = Anti_Forge_Token[0]  # 这里把第一个值放在之前定义的字典里面
            Anti_Forge_Code = re.findall("Code = \'(.+?)\'", t)
            # print(Anti_Forge_Code[0])
            tok["Anti_Forge_Code"] = Anti_Forge_Code[0]  # 这里把第二个值放在之前定义的字典里面
        except:
            print("获取token失败，请检查上面是否匹配正确")
            tok["Anti_Forge_Token"] = ""
            tok["Anti_Forge_Code"] = ""
        return tok

    def login(self, anti_token, user, psw):
        url2 = "https://passport.lagou.com/login/login.json"
        h2 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "X-Anit-Forge-Token": anti_token['Anti_Forge_Token'],
            "X-Anit-Forge-Code": anti_token['Anti_Forge_Code'],
            "Referer": "https://passport.lagou.com/login/login.html"
        }
        body = {
            "isValidate": "true",
            "username": user,
            "password": psw,
            "request_form_verifyCode": "",
            "submit": ""
        }

        self.s.headers.update(h2)
        # print(s.headers)
        r2 = self.s.post(url2, data=body, verify=False)
        # print(r2.text)
        return r2.json()


class DenglulgTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        cls.lsw = LaGouWang(cls.s)

    def test_token(self):
        token = self.lsw.gettoken()
        print(token)  # 先打印结果

        # 再断言

    def test_login(self):
        token = self.lsw.gettoken()
        result = self.lsw.login(token, "18651617370", "ef8284cb040218660698c329d4eb0775")
        print(result)  # 先打印结果
        # 再断言


if __name__ == "__main__":
    unittest.main()


