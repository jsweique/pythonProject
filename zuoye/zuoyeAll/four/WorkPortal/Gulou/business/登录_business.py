import time

import ddddocr
from PIL import Image

# from Gulou.config.browser import Browser
from zuoye.zuoyeAll.four.WorkPortal.Gulou.config.browser import Browser


class Login:
    def __init__(self, browser):
        self.browser = browser

    def image(self, src):
        self.browser.driver.save_screenshot(r"{}\photo0005.png".format(src))
        imgelement = self.browser.driver.find_element_by_class_name('login-code')  # 定位验证码
        location = imgelement.location  # 获取验证码x,y轴坐标
        # print(location)
        size = imgelement.size  # 获取验证码的长宽
        # print(size)
        rangle = (int(location['x'] + 340), int(location['y'] + 146), int(location['x'] + size['width'] + 380),    # 打开浏览器模式
                  int(location['y'] + size['height'] + 152))  # 写成我们需要截取的位置坐标(前两个代表定位位置，第三个代表离第一个点的宽度，第四个代表离第一个点的高度)
        i = Image.open(r"{}\photo0005.png".format(src))  # 打开截图
        frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4 = frame4.convert('RGB')
        frame4.save(r"{}\photo0006.png".format(src))  # 保存我们接下来的验证码图片 进行打码
        time.sleep(1)
        ocr = ddddocr.DdddOcr()
        with open(r"{}\photo0006.png".format(src), 'rb') as f:
            img_bytes = f.read()
        image = ocr.classification(img_bytes)
        #print(image)
        return image

    def login(self,username,password):
        print("登录操作 ：$")
        time.sleep(1)
        self.browser.driver.find_elements_by_class_name('el-input__inner')[0].send_keys(username)
        time.sleep(1)
        self.browser.driver.find_elements_by_class_name('el-input__inner')[1].send_keys(password)
        time.sleep(1)
        Flag = True
        i= 0
        while Flag:
            i = i +1
            if i ==11:
                break
            image = self.image(r'C:\yanzhengma')
            time.sleep(1)
            self.browser.driver.find_elements_by_class_name('el-input__inner')[2].clear()
            time.sleep(1)
            self.browser.driver.find_elements_by_class_name('el-input__inner')[2].send_keys(image)
            time.sleep(1)
            self.browser.driver.find_element_by_xpath('//span[contains(text(),"登")]').click()
            time.sleep(3)
            if self.browser.driver.title == '个人工作台 - 智慧鼓楼工作门户':
                Flag = False
                continue

            time.sleep(2)
        try:
            self.browser.driver.find_element_by_class_name("user-avatar")
        except:
            print("登录失败，用户名称:"+str(username) + "；密码是：" + str(password))
            # print("调用登录时打印：当前页面的title是："+  self.browser.driver.title)
            time.sleep(10)
            print("--------------------------------------------------------------------------------")
            return False  # 登录失败

        else:
            print("登录成功，用户名称:"+str(username))
            # print("调用登录时打印：当前页面的title是："+  self.browser.driver.title)
            time.sleep(1)
            print("--------------------------------------------------------------------------------")
            return True
            # 结果在哪里用在哪里返回


# 测试执行器
if  __name__=='__main__':
    br = Browser("http://192.168.20.243:9083/")
    br.browser()
    Login(br).login("jswq168","xsw2CDE#168")
    br.driver.close()