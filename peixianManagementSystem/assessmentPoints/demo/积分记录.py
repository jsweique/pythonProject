import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class PointsRecord:
    def __init__(self, login):
        self.login = login

    def query_points(self):
        self.login.driver.find_element_by_partial_link_text('后台数据管理').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('考核积分').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('考核积分').send_keys(Keys.PAGE_DOWN)  # 左侧菜单滑动到底部
        time.sleep(2)
        self.login.driver.find_element_by_link_text('积分记录').click()
        time.sleep(2)
        iframe = self.login.driver.find_element_by_xpath("//div[@class='tabs-panels']//div[2]//div[1]//iframe[1]")
        self.login.driver.switch_to.frame(iframe)
        time.sleep(1)
        Select(self.login.driver.find_element_by_id('department_2')).select_by_visible_text('沛城街道')
        time.sleep(1)
        Select(self.login.driver.find_element_by_id('department_1')).select_by_visible_text('新风居')
        time.sleep(1)
        Select(self.login.driver.find_element_by_id('department_0')).select_by_visible_text('新风网格1')
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_query').click()
        time.sleep(2)
        try:
            name = self.login.driver.find_element_by_xpath("//div[@class='container-fluid']//tr[1]//td[3]").text
            print('查询到用户的积分，用户为：{}'.format(name))
        except:
            print('未查询到用户')
        self.login.driver.close()

# driver=webdriver.Chrome()
