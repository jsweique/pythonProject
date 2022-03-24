import time
import ddddocr
from PIL import Image
from selenium import webdriver

class LoginBusiness:
    def __init__(self,url,username,password ):
        self.url = url
        self.username = username
        self.password = password

    #登录
    def login(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)

        self.driver.find_elements_by_class_name('el-input__inner')[0].send_keys(self.username)
        time.sleep(1)
        self.driver.find_elements_by_class_name('el-input__inner')[1].send_keys(self.password)
        time.sleep(1)

        #验证码循环3遍
        for i in range(5):
            self.driver.save_screenshot(r"C:\yanzhengma\photo0001.png")
            code = self.driver.find_element_by_xpath("//*[@class='login-code']")
            location = code.location
            size = code.size
            # Point = (int(location['x'] + 1320), int(location['y'] + 570),
            #          int(location['x'] + size['width'] + 1430),
            #          int(location['y'] + size['height'] + 610))
            Point  = (int(location['x'] +340), int(location['y'] +146),
                       int(location['x'] + size['width'] +380),
                       int(location['y'] + size['height'] + 152))

            I = Image.open(r"C:\yanzhengma\photo0001.png").crop(Point)
            I.save(r"C:\yanzhengma\photo0002.png")

            ocr = ddddocr.DdddOcr()
            with open(r"C:\yanzhengma\photo0002.png", 'rb') as f:
                img_bytes = f.read()
            T = ocr.classification(img_bytes)

            self.driver.find_elements_by_class_name('el-input__inner')[2].clear()
            self.driver.find_elements_by_class_name('el-input__inner')[2].send_keys(T)
            time.sleep(5)

            self.driver.find_element_by_css_selector("button").click()
            time.sleep(3)

            if self.driver.title == '个人工作台 - 智慧鼓楼工作门户':
                 print("用户"+self.username)
                 break
            else:
                 continue

        try:
                self.driver.find_element_by_class_name("user-avatar")
        except:
                print("登录失败")
                print("调用登录时打印：当前页面的title是：" + self.driver.title)
                time.sleep(10)
                print("--------------------------------------------------------------------------------")
                return False  # 登录失败

        else:
                print("登录成功")
                print("调用登录时打印：当前页面的title是：" + self.driver.title)
                time.sleep(1)
                print("--------------------------------------------------------------------------------")
                return True

    #关闭浏览器
    def close(self):
        self.driver.quit()
