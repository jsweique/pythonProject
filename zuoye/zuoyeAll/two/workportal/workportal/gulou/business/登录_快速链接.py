import time
import ddddocr
from PIL import Image
from selenium import webdriver


class BusinessCenter:
    def __init__(self,url,username,password):
         self.url = url
         self.username = username
         self.password = password

    def login_business_center(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)

        for i in range(3):
            self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/input[1]').clear()
            self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/input[1]').send_keys(self.username)
            time.sleep(2)
            self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[2]/input[1]').clear()
            self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[2]/input[1]').send_keys(self.password)
            time.sleep(2)
            self.driver.save_screenshot(r"E:\yanzhengma\photo0001.png")
            code =self.driver.find_element_by_xpath("//div[@class='login-code']")
            location =code.location
            size =code.size

            ran = (int(location['x'] + 340), int(location['y'] + 146),
                     int(location['x'] + size['width'] + 380),
                     int(location['y'] + size['height'] + 152))

            i = Image.open(r"E:\yanzhengma\photo0001.png").crop(ran)
            i.save(r"E:\yanzhengma\photo0002.png")

            ocr = ddddocr.DdddOcr()
            with open(r"E:\yanzhengma\photo0002.png", 'rb') as f:
                img_bytes = f.read()
            t = ocr.classification(img_bytes)
            self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[2]/input[1]').clear()
            self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[2]/input[1]').send_keys(t)
            time.sleep(3)
            self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[5]/div[1]/button[1]/span[1]/span[1]').click()
            time.sleep(2)
            if self.driver.title == '个人工作台 - 智慧鼓楼工作门户':
                break
            else:
                print('登录失败，再次登录')
                continue

    def close_web(self):
        self.driver.quit()


