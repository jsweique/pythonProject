import time
from PIL import Image
import pytesseract
from selenium import webdriver


class Login:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    # 获取列表中的数字，并转成字符串
    def tes(self, list):
        self.list = list
        list1 = []
        for i in self.list:
            if i.isdigit():
                list1.append(i)
        return ''.join(list1)

    # 获取验证码图片
    def image(self, src):
        self.driver.save_screenshot(r"{}\photo0001.png".format(src))
        imgelement = self.driver.find_element_by_id('imgCode')  # 定位验证码
        location = imgelement.location  # 获取验证码x,y轴坐标
        # print(location)
        size = imgelement.size  # 获取验证码的长宽
        # print(size)
        rangle = (int(location['x'] + 310), int(location['y'] + 130), int(location['x'] + size['width'] + 320),
                  int(location['y'] + size['height'] + 135))  # 写成我们需要截取的位置坐标(前两个代表定位位置，第三个代表离第一个点的宽度，第四个代表离第一个点的高度)
        i = Image.open(r"{}\photo0001.png".format(src))  # 打开截图
        frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4 = frame4.convert('RGB')
        frame4.save(r"{}\photo0002.png".format(src))  # 保存我们接下来的验证码图片 进行打码
        # time.sleep(3)
        pytesseract.pytesseract.tesseract_cmd = 'C:/Tesseract-OCR/tesseract.exe'
        tessdata_dir_config = '--tessdata-dir "C:/Tesseract-OCR/tessdata"'
        image = Image.open(r"{}\photo0002.png".format(src))
        return image

    def login(self):
        # self.options = webdriver.ChromeOptions()
        # # 添加无界面参数
        # self.options.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=self.options)
        # print("1")
        # self.driver.get(self.url)
        # print("2")
        # self.driver.maximize_window()

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        self.driver.maximize_window()

        print(self.driver.title)

        Flag = True
        while Flag:
            image = self.image(r'C:\yanzhengma')
            self.driver.find_element_by_id('loginname').clear()
            time.sleep(1)
            self.driver.find_element_by_id('loginname').send_keys(self.username)
            time.sleep(1)
            self.driver.find_element_by_id('password').clear()
            time.sleep(1)
            self.driver.find_element_by_id('password').send_keys(self.password)
            time.sleep(1)
            list2 = list(pytesseract.image_to_string(image))
            t = self.tes(list2)
            self.driver.find_element_by_id('ValidateCode').clear()
            time.sleep(1)
            self.driver.find_element_by_id('ValidateCode').send_keys(t)
            time.sleep(1)
            self.driver.find_element_by_id('btnSubmit').click()
            time.sleep(5)
            if self.driver.title == '市域社会治理' or self.driver.title == '社会综合治理':
                Flag = False
                continue
            self.driver.find_element_by_id('imgCode').click()
            time.sleep(3)
            #return self.driver
