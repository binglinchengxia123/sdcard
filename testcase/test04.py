import os
import unittest

path = 'C:/Users/MBENBEN/Pictures'
files = os.listdir(path)

class HowToFindFileTestCase(unittest.TestCase):
    def testFindFile(self):
        for f in files:
            if 'off' in f and f.endswith('.png'):
                print('find it! ' + f)
            else:
                print("missing target!")

if __name__ == '__main__':
    unittest.main()