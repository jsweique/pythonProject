from time import sleep
from selenium.webdriver.support import expected_conditions as EC  #标题判断

from selenium import webdriver



class Browser():
    def __init__(self, url):
        self.url = url


    #0，封装打开浏览器
    def browser(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(2)
        print("--------------------------------------------------------------------------------")

    #1，标题判断，返回True  或者 False
    def assert_title1(self, title_name=None):   # 判断当前title是否正确
        # 判断当前title是否正确
        if title_name != None:
            get_title = EC.title_contains(title_name)
            return get_title(self.driver)

    #1，标题判断，返回成功或失败
    def assert_title2(self, tittle_name=None):
        if tittle_name != None:
            get_tittle = EC.title_contains(tittle_name)
            result = get_tittle(self.driver)
            if result == True:
                print("标题切换成功，判断成功，当前标题为："+ str(self.driver.title))
                print("--------------------------------------------------------------------------------")
                return True
            else:
                print("标题判断错误***！！！，当前标题为：" + str(self.driver.title),"不是本次标题："+str(tittle_name))
                print("--------------------------------------------------------------------------------")
                return False
        else:
            print("标题判断失败，标题为空")
            print("--------------------------------------------------------------------------------")
            return False

    #3，切合窗口
    def switch_windows3(self, title_name=None):   # title的名称
        handl_list = self.driver.window_handles
        # print(handl_list)
        current_handle = self.driver.current_window_handle
        for i in handl_list:
            if i != current_handle:
                sleep(2)
                # print("切换到窗口：" + str(self.browser.driver.title))
                self.driver.switch_to.window(i)
                if self.assert_title1(title_name):  # 当前窗口title_name
                    break
        # print("切换到窗口：" + str(self.driver.title))

    #4，切换窗口，并判断标题
    def switch_windows4(self,title_name):
        self.switch_windows3(title_name)
        self.assert_title2(title_name)

    # 5，切换窗口 + 判断
    def switch_windows5(self, title_name=None):   # title的名称
        handl_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in handl_list:
            if i != current_handle:
                sleep(2)
                self.driver.switch_to.window(i)
                print("切换到窗口：" + str(self.driver.title))
                if str(self.driver.title) == str(title_name):  # 当前窗口title_name
                    break
        else:
            print("没有此窗口：" + str(title_name))
            return False
        print("确认窗口：" + str(self.driver.title))


if  __name__=='__main__':
    br = Browser("http://192.168.20.243:9083")
    br.browser()
    br.assert_title2('作门户')


