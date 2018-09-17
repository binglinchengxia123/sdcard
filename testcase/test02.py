import os

path = 'C:/Users/MBENBEN/Pictures'
files = os.listdir(path)

for f in files:
    if 'off' in f and f.endswith('.png'):
        print('find it! '+f)