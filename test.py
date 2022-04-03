#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/4/3
# @File Name: test.py


import requests
url = "http://127.0.0.1:8000/upload"
path = "main.py"
files = {'file': open(path, 'rb')}
r = requests.post(url, files=files)
print(r.url)
print(r.text)
