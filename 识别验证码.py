import ddddocr
import requests
from selenium import webdriver

#识别验证码
ocr = ddddocr.DdddOcr()
with open(r'C:\Users\zheng\Desktop\微信截图_20211204135139.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
print(res)
print(type(res))

# 获取验证码连接，验证码图片保存到本地   (指挥调度无法获取)
# web = webdriver.Chrome()
# web.get(r'http://192.168.20.211:2032/')
# w = web.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[3]/img')
# print(w.get_attribute('src'))
# r = requests.get(w.get_attribute('src'))#获取标签属性值
# with open(r'C:\Users\zheng\Desktop\2234.png', 'wb') as w:
#     w.write(r.content)

