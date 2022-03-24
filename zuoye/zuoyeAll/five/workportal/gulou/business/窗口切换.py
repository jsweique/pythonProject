import time


class WindowSwitch:
    '''
    业务中台切换窗口句柄
    '''

    def __init__(self, login):
        self.login = login

    def swtich_last(self, name):
        '''
        根据业务中台中配置的名称切换窗口
        :param name:
        :return:
        '''
        self.login.driver.find_element_by_xpath("//li[contains(text(),'应用中心')]").click()
        time.sleep(1)
        self.login.driver.find_elements_by_xpath("//h4[contains(text(),'{}')]".format(name))[0].click()
        time.sleep(3)
        self.login.driver.switch_to.window(self.login.driver.window_handles[-1])

    def switch_first(self):
        '''
        切换到业务中台首页
        :return:
        '''
        self.login.driver.switch_to.window(self.login.driver.window_handles[0])
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//li[contains(text(),'个人工作台')]").click()
        time.sleep(1)
