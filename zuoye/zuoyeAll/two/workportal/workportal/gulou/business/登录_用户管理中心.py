import time
import ddddocr
from PIL import Image
from selenium import webdriver


class BusinessCenter: #定义登录类
    def __init__(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password

    def login_business_center(self): #定义登录
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)

        for i in range(5):   #循环登录     #登录账号密码验证码
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
            self.driver.save_screenshot(r"C:\yanzhengma\photo0001.png")
            code =self.driver.find_element_by_xpath("//div[@class='login-code']")
            location =code.location
            size =code.size

            ran = (int(location['x'] + 340), int(location['y'] + 146),
                     int(location['x'] + size['width'] + 380),
                     int(location['y'] + size['height'] + 152))

            i = Image.open(r"C:\yanzhengma\photo0001.png").crop(ran)
            i.save(r"C:\yanzhengma\photo0002.png")

            ocr = ddddocr.DdddOcr()  #第三方处理验证码
            with open(r"C:\yanzhengma\photo0002.png", 'rb') as f:
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
            if self.driver.title == '个人工作台 - 智慧鼓楼工作门户':  #判断标题
                break
            else:
                print('登录失败，再次登录')
                continue


    def application_center(self):  #应用中心
        self.driver.find_element_by_xpath("//div[@class='el-row']//li[7]").click()
        time.sleep(3)
        self.driver.find_elements_by_xpath("// h4[contains(text(), '用户中心')]")[0].click()
        time.sleep(3)



    def new_window (self):  # 切换窗口
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])  # 切换到第二窗口
        time.sleep(2)
        self.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/div[3]/li[1]/div[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/div[3]/li[1]/ul[1]/div[1]/a[1]/li[1]').click()
        time.sleep(2)


    def close_web(self):  #关闭浏览器
        self.driver.quit()


