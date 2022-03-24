import random
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TaskManagement:
    def __init__(self, login):
        self.login = login

    def add_task(self):
        self.login.driver.find_element_by_partial_link_text('后台数据管理').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('巡查走访').click()
        # time.sleep(1)
        # self.login.driver.find_element_by_link_text('巡查走访').send_keys(Keys.PAGE_DOWN)  # 左侧菜单滑动到底部
        time.sleep(2)
        self.login.driver.find_element_by_partial_link_text('考核任务管理').click()
        time.sleep(2)
        iframe = self.login.driver.find_element_by_xpath("//div[@class='tabs-panels']//div[2]//div[1]//iframe[1]")
        self.login.driver.switch_to.frame(iframe)
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_create').click()
        time.sleep(2)
        self.login.driver.find_element_by_id('select2-DepartmentId-container').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//input[@class='select2-search__field']").send_keys('新风网格1')
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//input[@class='select2-search__field']").send_keys(Keys.ENTER)
        time.sleep(1)
        Select(self.login.driver.find_element_by_id('RoleId')).select_by_value('0436a86e-2ad6-4e48-b34f-151356554734')
        global name
        name = '自动化测试任务' + str(random.randint(1, 50))
        self.login.driver.find_element_by_id('Name').send_keys(name)
        time.sleep(1)
        self.login.driver.find_element_by_id('IsEnabled').click()
        time.sleep(1)
        Select(self.login.driver.find_element_by_id('EnumMissionType')).select_by_visible_text('事件')
        time.sleep(1)
        self.login.driver.find_element_by_id('PlanNum').clear()
        time.sleep(1)
        self.login.driver.find_element_by_id('PlanNum').send_keys('5')
        time.sleep(1)
        Select(self.login.driver.find_element_by_id('EnumMissitonDateType')).select_by_visible_text('每周')
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_sub').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        time.sleep(3)
        self.login.driver.find_element_by_id('keyword').send_keys(name)
        time.sleep(1)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(3)
        try:
            if self.login.driver.find_element_by_xpath('//tr[1]//td[4]').text == name:
                print('{}任务新增成功'.format(name))
            else:
                print('任务新增失败')
        except:
            print('任务新增失败，报异常')

    def disable_task(self):
        global name
        self.login.driver.find_element_by_id('keyword').clear()
        time.sleep(1)
        self.login.driver.find_element_by_id('keyword').send_keys(name)
        time.sleep(1)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath('//tr[1]//td[2]//a[3]//span[1]').click()
        time.sleep(2)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(2)
        try:
            if self.login.driver.find_element_by_xpath('//tr[1]//td[5]').text == '否':
                print('禁用任务成功')
            else:
                print('禁用任务失败')
        except:
            print('禁用任务失败，报异常')

    def edit_task(self):
        global name
        self.login.driver.find_element_by_id('keyword').clear()
        time.sleep(1)
        self.login.driver.find_element_by_id('keyword').send_keys(name)
        time.sleep(1)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath('//tr[1]//td[2]//a[2]//span[1]').click()
        time.sleep(2)
        self.login.driver.find_element_by_id('IsEnabled').click()
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_sub').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        time.sleep(3)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(2)
        try:
            if self.login.driver.find_element_by_xpath('//tr[1]//td[5]').text == '是':
                print('启用任务成功')
            else:
                print('启用任务失败')
        except:
            print('启用任务失败，报异常')
        self.login.driver.close()

