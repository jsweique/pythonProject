import ddddocr
import requests
from selenium import webdriver


'''
无法使用：
打开页面显示的验证码与调用接口获取的验证码不同！！！
'''
web=webdriver.Chrome()
web.get(r'http://192.168.20.214:10001/')
yzm=web.find_element_by_class_name('yzm')
src=yzm.get_attribute('src')
resp=requests.get(src)
with open(r'img.png',mode='wb') as w:
    w.write(resp.content)
ocr = ddddocr.DdddOcr()
res = ocr.classification(resp.content)
print(res)