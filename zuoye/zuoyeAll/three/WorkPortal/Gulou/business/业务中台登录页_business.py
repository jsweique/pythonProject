import time #导入时间

import ddddocr #文件导入
from PIL import Image
from selenium import webdriver

class LoginBusinessCenter:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def login_bussiness_center(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() #最大化浏览器
        self.driver.get(self.url)

        for i in range(5):
            self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/input[1]').clear()
            self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/input[1]').send_keys(
                self.username)
            time.sleep(1)
            self.driver.find_element_by_xpath('//form[1]/div[3]/div[1]/div[1]/div[2]/input[1]').clear()
            self.driver.find_element_by_xpath('//form[1]/div[3]/div[1]/div[1]/div[2]/input[1]').send_keys(self.password)
            time.sleep(1)
            self.driver.save_screenshot(r"C:\yanzhengma\photo0001.png") #截图存放地址
            code = self.driver.find_element_by_xpath("//*[@class='login-code']")  #查找验证码
            location = code.location #查找坐标
            size = code.size #获取验证码
            rangle = (int(location['x'] + 340), int(location['y'] + 146),
                      int(location['x'] + size['width'] +380),
                      int(location['y'] + size['height'] + 152))
            i = Image.open(r"C:\yanzhengma\photo0001.png").crop(rangle) #打开验证码图片
            i.save(r"C:\yanzhengma\photo0002.png") #保存验证码
            ocr = ddddocr.DdddOcr()
            with open(r"C:\yanzhengma\photo0002.png", 'rb') as f:
                img_bytes = f.read()
            t = ocr.classification(img_bytes) #识别验证码
            self.driver.find_elements_by_class_name('el-input__inner')[2].clear()
            self.driver.find_elements_by_class_name('el-input__inner')[2].send_keys(t) #验证信息
            time.sleep(3)
            self.driver.find_element_by_css_selector("button").click()#点击登录
            time.sleep(3)
            if self.driver.title == '个人工作台 - 智慧鼓楼工作门户':
                break
            else:
                print('登录失败，再次登录')
                continue

