import unittest
from ddt import ddt,data,file_data,unpack

@ddt
class demotest(unittest.TestCase):

    def setUp(self):
        print("this is the setup")

    #@data(2,3,4)
    @data("iphone","xiaomi","chuizi")
    def testb(self, value1):
        print(value1)
        # print(value2)
        # print(value3)
        print("this is testb")


if __name__ == "__main__":
    unittest.main()



