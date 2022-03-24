import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class PointsSummary:
    def __init__(self, login):
        self.login = login

    def query_point(self):
        self.login.driver.find_element_by_partial_link_text('后台数据管理').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('考核积分').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('考核积分').send_keys(Keys.PAGE_DOWN)  # 左侧菜单滑动到底部
        time.sleep(2)
        self.login.driver.find_element_by_partial_link_text('积分汇总').click()
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
        time.sleep(1)
        try:
            self.login.driver.find_element_by_xpath("//div[@class='container-fluid']//tr[1]//td[1]").text is not None
            print('查询到用户')
        except:
            print('未查询到用户')
        self.login.driver.close()
