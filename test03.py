import time

from PIL import Image
import pytesseract
from selenium.webdriver import Chrome
from aip import AipOcr

# web = Chrome()
# web.get('http://www.chaojiying.com/user/login/')
# time.sleep(2)
# web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('123456')
# time.sleep(2)
# png = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
# # with open('./imgg.png', mode='wb') as w:
# #     w.write(png)
APP_ID = '25218737'
API_KEY = '0uTWuOtGyEnTVpB7NgeD6Hx9'
SECRET_KEY = 'TPRevIqNlsuAQoXMriY0CyzcEOYg0vkZ'

image = Image.open('./55.png')
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < 147:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
image.save('./56.png')
with open('./56.png', mode='rb') as f:
    img = f.read()
baidu_api = AipOcr(APP_ID, API_KEY, SECRET_KEY)
result = baidu_api.handwriting(img)
print(result)


# r=pytesseract.image_to_string('./56.png')
# print(r)