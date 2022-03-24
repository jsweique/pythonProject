from time import sleep

from selenium import webdriver



class Browser():
    def __init__(self, url):
        self.url = url



    def browser(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        #self.driver.maximize_window()
        sleep(2)
        print("调用浏览器打印：当前页面的title是："+ self.driver.title)
        sleep(1)
        print("--------------------------------------------------------------------------------")


if  __name__=='__main__':
    Browser("http://192.168.20.243:8081/login").browser()
