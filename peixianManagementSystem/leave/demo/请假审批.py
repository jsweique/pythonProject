import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class ApproveLeave:
    def __init__(self, login):
        self.login = login

    def approve_leave(self):
        self.login.driver.find_element_by_partial_link_text('后台数据管理').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('请假管理').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('请假管理').send_keys(Keys.PAGE_DOWN)  # 左侧菜单滑动到底部
        time.sleep(2)
        self.login.driver.find_element_by_partial_link_text('请假审批').click()
        time.sleep(2)
        iframe = self.login.driver.find_element_by_xpath("//div[@class='tabs-panels']//div[2]//div[1]//iframe[1]")
        self.login.driver.switch_to.frame(iframe)
        time.sleep(1)
        Select(self.login.driver.find_element_by_id('EnumApproveStatus')).select_by_visible_text('待审批')
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_query').click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath(
            '//body[1]/div[2]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/a[1]').click()
        time.sleep(2)
        self.login.driver.find_element_by_id('btn_receive').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[contains(@class,'layui-layer-btn0')]").click()
        print('审批请假成功')
        time.sleep(2)
        self.login.driver.close()




