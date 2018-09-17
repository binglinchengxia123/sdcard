# coding:utf-8

import unittest
import os
from common import HTMLTestRunner_cn

curpath = os.path.dirname(os.path.realpath(__file__))
print(curpath)
casepath = os.path.join(curpath, "testcase")
print(casepath)


# start_dir = r"G:\unittest\testcase"
pattern = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casepath,pattern=pattern)
# print(discover)

# runner = unittest.TextTestRunner()
# runner.run(discover)

reportpath = os.path.join(curpath,"report","report.html")
#   报告的存放路径地址，使用join方法合并目录名字
fp = open(reportpath, "wb")

runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                          title="测试报告",
                                          description="测试结果详情")

runner.run(discover)