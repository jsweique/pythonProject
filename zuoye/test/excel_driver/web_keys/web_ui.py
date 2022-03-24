'''
关键字驱动
'''
from time import sleep

from selenium import webdriver


# 使用反射，根据type_的值创建浏览器对象
def browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except:
        print('出现异常，启动默认浏览器Chrome')
        driver = webdriver.Chrome()
    return driver


class WebDemo:
    def __init__(self, type_):
        self.driver = browser(type_)

    def open(self, **kwargs):
        self.driver.get(kwargs['txt'])

    def locator(self, **kwargs):
        return self.driver.find_element(kwargs['name'], kwargs['value'])

    def input(self, **kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])

    def click(self, **kwargs):
        self.locator(**kwargs).click()

    def quit(self, **kwargs):
        self.driver.quit()

    def wait(self, **kwargs):
        sleep(kwargs['txt'])
