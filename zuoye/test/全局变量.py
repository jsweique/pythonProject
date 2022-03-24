import random
import time

import ddddocr
from PIL import Image
from selenium import webdriver


class OverallSituationTest:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def overall_situation_test(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.maximize_window()
        self.driver = driver
        # return self.driver

    def test_login(self):
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
            self.driver.save_screenshot(r"c:\yanzhengma\photo0001.png")
            code = self.driver.find_element_by_xpath("//*[@class='login-code']")
            location = code.location
            size = code.size
            ran = (int(location['x'] + 340), int(location['y'] + 146),
                   int(location['x'] + size['width'] + 380),
                   int(location['y'] + size['height'] + 152))
            i = Image.open(r"C:\yanzhengma\photo0001.png").crop(ran)
            i.save(r"C:\yanzhengma\photo0002.png")
            ocr = ddddocr.DdddOcr()
            with open(r"C:\yanzhengma\photo0002.png", 'rb') as f:
                img_bytes = f.read()
            t = ocr.classification(img_bytes)
            self.driver.find_elements_by_class_name('el-input__inner')[2].clear()
            self.driver.find_elements_by_class_name('el-input__inner')[2].send_keys(t)
            time.sleep(2)
            self.driver.find_element_by_css_selector("button").click()
            time.sleep(2)
            if self.driver.title == '个人工作台 - 智慧鼓楼工作门户':
                break
            else:
                print('登录失败，再次登录')
                continue


class TestOverall:
    def __init__(self):
        pass

    def a(self):
        c = 5
        self.c = c

    def b(self):
        print(self.c)


# t=TestOverall()
# t.a()
# t.b()

def draw():
    names = ['宋心语', '昝帅', '苏慕文', '董文静', '高加芹','郑新洋']
    titles = ['用户管理', '角色管理', '部门管理']
    new_names = []
    while True:
        r = random.choice(names)
        if r not in new_names:
            new_names.append(r)
            if len(new_names) == 6:
                break
    ss = {titles[0]: [new_names[0], new_names[1]], titles[1]: [new_names[2], new_names[3]],
          titles[2]: [new_names[4], new_names[5]]}
    print(ss)