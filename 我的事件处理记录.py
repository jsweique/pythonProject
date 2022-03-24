import time

from selenium import webdriver


class MyEvents:
    def __init__(self, login, code):
        self.login = login
        self.code = code

    def my_events(self):
        # self.login.driver.find_element_by_link_text('后台管理控制').click()
        # time.sleep(1)
        self.login.driver.find_element_by_link_text('后台数据管理控制台').click()
        time.sleep(2)
        self.login.driver.find_elements_by_link_text('事件处置中心')[-1].click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('我的事件处理记录').click()
        time.sleep(1)
        frame = self.login.driver.find_element_by_xpath("//div[@class='tabs-panels']//div[2]//div[1]//iframe[1]")
        self.login.driver.switch_to.frame(frame)
        self.login.driver.find_element_by_id('EventRecordCode').send_keys(self.code)
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_query').click()
        time.sleep(1)

        try:
            code2 = self.login.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
            if self.code == code2:
                print('查询成功，单号：' + code2)
            else:
                print('未查询到单号')
        except:
            print('未查询到单号')
        self.login.driver.close()
#d=webdriver.Chrome()
#d.execute()
