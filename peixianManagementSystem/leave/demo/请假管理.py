import random
import time

from selenium.webdriver.common.keys import Keys


class LeaveManagement:
    def __init__(self, login):
        self.login = login

    # 新增请假类型
    def add_leave_management(self):
        self.login.driver.find_element_by_partial_link_text('后台数据管理').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('请假管理').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('请假管理').send_keys(Keys.PAGE_DOWN)  # 左侧菜单滑动到底部
        time.sleep(2)
        self.login.driver.find_element_by_link_text('请假类型').click()
        iframe = self.login.driver.find_element_by_xpath(
            "//div[@class='tabs-panels']//div[2]//div[1]//iframe[1]")  # 定位到右侧的iframe
        self.login.driver.switch_to.frame(iframe)
        time.sleep(1)

        self.login.driver.find_element_by_id('btn_create').click()
        time.sleep(1)
        global leave_type
        leave_type = '测试请假类型' + str(random.randint(1, 50))
        self.login.driver.find_element_by_id('Name').send_keys(leave_type)
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_sub').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        time.sleep(2)
        print('新增请假类型成功，请假类型为：{}'.format(leave_type))

        # self.login.driver.find_element_by_xpath("//input[@id='keyword']").send_keys('3')
        # time.sleep(1)

    def edit_leave_management(self):
        global leave_type
        time.sleep(1)
        self.login.driver.find_element_by_id('keyword').send_keys(leave_type)
        time.sleep(1)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='edit']").click()
        time.sleep(3)
        self.login.driver.find_element_by_id('Memo').send_keys(leave_type)
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_sub').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        time.sleep(3)
        print('编辑{}，保存成功'.format(leave_type))

    def delete_leave_management(self):
        global leave_type
        time.sleep(1)
        self.login.driver.find_element_by_id('keyword').clear()
        time.sleep(1)
        self.login.driver.find_element_by_id('keyword').send_keys(leave_type)
        time.sleep(1)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//input[@name='xuSelectItem']").click()
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_del').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        time.sleep(1)
        self.login.driver.find_element_by_id('query').click()
        try:
            self.login.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[4]')
        except:
            print('删除{}，请假类型成功'.format(leave_type))
        self.login.driver.close()

    def export_leave_management(self):
        pass

    def query_leave_management(self):
        global leave_type
        time.sleep(1)
        self.login.driver.find_element_by_id('keyword').send_keys(leave_type)
        time.sleep(1)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(2)
        try:
            t = self.login.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[4]').text
            if t == leave_type:
                print('查询到新增的请假类型：{}'.format(t))
            else:
                print('未查询到该请假类型')
        except:
            print('未查询到该请假类型')
        self.login.driver.find_element_by_xpath("//span[contains(@class,'glyphicon glyphicon-trash')]").click()
        time.sleep(1)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(2)
