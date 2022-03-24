import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class RuleSettings:
    def __init__(self, login):
        self.login = login

    def add_rule(self):
        self.login.driver.find_element_by_partial_link_text('后台数据管理').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('考核积分').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('考核积分').send_keys(Keys.PAGE_DOWN)  # 左侧菜单滑动到底部
        time.sleep(2)
        self.login.driver.find_element_by_partial_link_text('规则设置').click()
        time.sleep(2)
        iframe = self.login.driver.find_element_by_xpath("//div[@class='tabs-panels']//div[2]//div[1]//iframe[1]")
        self.login.driver.switch_to.frame(iframe)
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_create').click()
        time.sleep(2)
        Select(self.login.driver.find_element_by_id('EnumAssessmentType')).select_by_visible_text('事件')
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='btn btn-default btn-success']").click()
        time.sleep(2)
        self.login.driver.find_element_by_id('ztree_16_check').click()  # 选择的是“教育整顿意见建议”
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//button[@class='close']").click()
        time.sleep(1)
        self.login.driver.find_element_by_id('Score').clear()
        time.sleep(1)
        self.login.driver.find_element_by_id('Score').send_keys('10')
        time.sleep(1)
        self.login.driver.find_element_by_id('MaxScore').clear()
        time.sleep(1)
        self.login.driver.find_element_by_id('MaxScore').send_keys('25')
        time.sleep(1)
        self.login.driver.find_element_by_id('IsEnabled').click()
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_sub').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        time.sleep(2)
        global name
        name = '事件/教育整顿意见建议'
        self.login.driver.find_element_by_id('keyword').clear()
        self.login.driver.find_element_by_id('keyword').send_keys(name)
        time.sleep(1)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(2)
        try:
            if self.login.driver.find_element_by_xpath('//td[4]').text == name:
                print('考核项目新增成功：{}'.format(name))
            else:
                print('考核项目添加失败')
        except:
            print('考核项目添加失败，报异常')

    def edit_rule(self):
        global name
        self.login.driver.find_element_by_id('keyword').clear()
        self.login.driver.find_element_by_id('keyword').send_keys(name)
        time.sleep(1)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath('//tr[1]//td[2]//a[1]//span[1]').click()
        time.sleep(2)
        self.login.driver.find_element_by_id('Memo').send_keys('填写的备注信息')
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_sub').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        print('编辑考核项目成功')
        time.sleep(2)

    def disable_rule(self):
        global name
        self.login.driver.find_element_by_id('keyword').clear()
        self.login.driver.find_element_by_id('keyword').send_keys(name)
        time.sleep(1)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath('//tr[1]//td[2]//a[2]//span[1]').click()
        time.sleep(1)
        self.login.driver.find_element_by_id('query').click()
        time.sleep(2)
        try:
            if self.login.driver.find_element_by_xpath('//tr[1]//td[8]').text == '否':
                print('禁用考核项目成功')
            else:
                print('禁用考核项目失败')
        except:
            print('禁用考核项目失败，报异常')
        self.login.driver.close()

