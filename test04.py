import json
import re
import time
from lxml import etree

import requests
# from selenium.webdriver import Chrome
from selenium import webdriver

#
option = webdriver.ChromeOptions()
web = webdriver.Chrome(options=option)

# print(web.page_source)

# etre = etree.HTML(web.page_source)
# login = etre.xpath('//input[@class="login-code"]/img/@src')

# web.maximize_window()
# code=web.find_element_by_class_name('login-code')
# print(code.find_element_by_xpath('//img/@src'))
# time.sleep(5)
# web.refresh()


# time.time()#时间戳

# with open(r'C:\Users\zheng\Desktop\新建文本文档 (3).txt', mode='w',encoding='utf-8') as f:
#     f.write(r'第三行')
#     f.write("\n")
#     f.write('第四行')
from reptile_01.代理池 import TestProxy

# TestProxy().test()

res = requests.get(r'http://192.168.20.243:8081/prod-api/sys/getCode')
r = res.text
print(r)
test_list = r.split(',')
uuid = test_list[0].split(':')
str = uuid[1].strip('"')
resp = requests.get(r'http://192.168.20.243:8080/sys/codeNum?uuid={}'.format(str))
print(resp.text)

data = {
    "code": resp.text,
    "loginName": "pxsfj",
    "password": "123456",
    "rememberMe": False,
    "username": "pxsfj",
    "uuid": str
}
header = {
    'Host': '192.168.20.243:8081',
    'Origin': 'http://192.168.20.243:8081',
    'Referer': 'http://192.168.20.243:8081/login?redirect=%2Fdev%2Fdepartment',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '135',
    'Content-Type': 'application/json'
}
resp2 = requests.post('http://192.168.20.243:8081/prod-api/sys/login', json=data, headers=header)
print(resp2.text)
data2 = resp2.text.split('{')[2]
data2 = data2.split('}')[0]
data2 = '{' + data2 + '}'.strip()
print(data2)

toke=re.compile('"token":"(?P<token>.*?)"')
token2=toke.search(data2).group('token')
print(token2)
userId=re.compile('userId":"(?P<id>.*?)"')
userId2=userId.search(data2).group('id')
print(userId2)

# dict_resp2 = json.loads(data2)#字符串转字典
# print(dict_resp2)
# print(type(dict_resp2))

dict_resp2 = {'name': 'token', 'value': token2}
dict_resp3 = {'name': 'userId', 'value': userId2}

time.sleep(1)
web.get(r'http://192.168.20.243:8081/dashboard')
web.add_cookie(dict_resp2)
web.add_cookie(dict_resp3)
web.refresh()
