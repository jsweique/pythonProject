import time

import win32api
import win32con
from selenium import webdriver


class EventHandle:
    def __init__(self, login, code, name):
        self.login = login
        self.code = code
        self.name = name

    def event_handle(self):
        self.login.driver.find_element_by_link_text('后台管理控制').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('后台数据管理控制台').click()
        time.sleep(2)
        self.login.driver.find_elements_by_link_text('事件处置中心')[-1].click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('事件处置工作台').click()
        time.sleep(1)
        frame = self.login.driver.find_element_by_xpath("//div[@class='tabs-panels']//div[2]//div[1]//iframe[1]")
        self.login.driver.switch_to.frame(frame)
        self.login.driver.find_element_by_xpath("//input[@id='EventRecordCode']").send_keys(self.code)
        time.sleep(1)

        self.login.driver.find_element_by_id('btn_query').click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]/a').click()
        time.sleep(2)
        self.login.driver.switch_to.default_content()  # 切换回主页面
        time.sleep(1)
        frame = self.login.driver.find_element_by_xpath('//div[3]//div[1]//iframe[1]')
        self.login.driver.switch_to.frame(frame)
        self.login.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_show_transit').click()
        time.sleep(1)
        self.login.driver.find_element_by_id('transittingContext').send_keys('本部门处理不了该事件，移交到你部门处理！')
        time.sleep(1)
        self.login.driver.find_element_by_id('select2-transitDepartId-container').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath(
            "//span[@class='select2-search select2-search--dropdown']//input[@class='select2-search__field']").send_keys(
            '沛县公安局')
        time.sleep(1)
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_transit').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        time.sleep(1)

        self.login.driver.switch_to.default_content()  # 切换回
        # 主页面
        time.sleep(1)
        frame = self.login.driver.find_element_by_xpath("//div[@class='tabs-panels']//div[2]//div[1]//iframe[1]")
        self.login.driver.switch_to.frame(frame)
        time.sleep(1)
        self.login.driver.find_element_by_id('EventRecordCode').clear()
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_query').click()
        time.sleep(3)


# d = webdriver.Chrome()
