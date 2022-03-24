import random

import requests
from selenium import webdriver

url=r'http://www.baidu.com'
proxy={
    "http": "http://124.77.82.32:9000",
    "https": "https://124.77.82.32:9000"
}
# resp=requests.get(url,proxies=proxy)
# resp.encoding='utf-8'
# print(resp.text)
# print(resp.status_code)

# web=webdriver.Chrome()
# web.get(r'http://192.168.20.214:9025/')
# src=web.find_element_by_id('imgCode').get_attribute('src')
# print(src)


codes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
c = []
while True:
    c.append(random.choice(codes))
    if len(c) == 5:
        break
type_management_code = ''.join(c)
print(type(type_management_code))
print(type_management_code)