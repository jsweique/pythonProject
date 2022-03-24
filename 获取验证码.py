import random
import time

import pytesseract
from PIL import Image
from selenium import webdriver


def image(src):
    driver.save_screenshot(r"{}\photo0001.png".format(src))
    imgelement = driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/div[2]/img')  # 定位验证码
    location = imgelement.location  # 获取验证码x,y轴坐标
    # print(location)
    size = imgelement.size  # 获取验证码的长宽
    # print(size)
    rangle = (int(location['x'] + 0), int(location['y'] + 0), int(location['x'] + size['width'] + 0),
              int(location['y'] + size['height'] + 0))  # 写成我们需要截取的位置坐标(前两个代表定位位置，第三个代表离第一个点的宽度，第四个代表离第一个点的高度)
    i = Image.open(r"{}\photo0001.png".format(src))  # 打开截图
    frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4 = frame4.convert('RGB')
    t = random.randint(0, 10000000000)
    frame4.save(r'C:\xunlian\3\\' + str(t)+'.jpg')  # 保存我们接下来的验证码图片 进行打码
    # time.sleep(3)
    pytesseract.pytesseract.tesseract_cmd = 'C:/Tesseract-OCR/tesseract.exe'
    tessdata_dir_config = '--tessdata-dir "C:/Tesseract-OCR/tessdata"'
    # image = Image.open(r"{}\photo0002.png".format(src))
    # return image


option=webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(options=option)
driver.get(r'http://192.168.20.243:8081/')
driver.maximize_window()
for i in range(20000):
    image(r'C:\xunlian\1')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/div[2]/img').click()
    time.sleep(1)


driver.close()


