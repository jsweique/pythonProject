import datetime
import random
import socket
import time

import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

'''
WebDriverWait().until(expected_conditions.element_to_be_clickable((BY.NAME,"")))
WebDriverWait().until(expected_conditions.element_to_be_selected())
'''
'''
#不启动浏览器执行
option=webdriver.ChromeOptions()
option.add_argument('headless')
d = webdriver.Chrome(options=option)
'''
# 解析域名
#print(socket.gethostbyname('47test.jsweique.com'))

# 识别图片
image = Image.open(R'C:\Users\zheng\Desktop\1136-interferenceline.jpg')
print(pytesseract.image_to_string(image))


# driver = webdriver.Firefox()
#
# driver.get(r'http://192.168.20.214:10001')
# print(driver.find_elements_by_tag_name('input'))
# driver.maximize_window()
# driver.find_element_by_id('loginname').send_keys(Keys.CONTROL, 'V')
# time.sleep(5)
# driver.close()
