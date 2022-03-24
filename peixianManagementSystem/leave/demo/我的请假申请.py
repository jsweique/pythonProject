import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from 文件上传 import UploadFile


class MyLeave:
    def __init__(self, login):
        self.login = login

    def add_my_leave(self):
        self.login.driver.find_element_by_partial_link_text('后台数据管理').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('请假管理').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('请假管理').send_keys(Keys.PAGE_DOWN)  # 左侧菜单滑动到底部
        time.sleep(2)
        self.login.driver.find_element_by_partial_link_text('我的请假列表').click()
        time.sleep(2)
        iframe = self.login.driver.find_element_by_xpath("//div[@class='tabs-panels']//div[2]//div[1]//iframe[1]")
        self.login.driver.switch_to.frame(iframe)
        self.login.driver.find_element_by_id('btn_create').click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath(
            "//div[@id='dtp_StartTime']//i[@class='glyphicon glyphicon-calendar']").click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath('//body[1]/div[1]/div[3]/table[1]/tfoot[1]/tr[1]/th[1]').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath(
            "//div[@id='dtp_EndTime']//i[@class='glyphicon glyphicon-calendar']").click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//body[1]/div[2]/div[3]/table[1]/tfoot[1]/tr[1]/th[1]").click()
        time.sleep(1)
        Select(self.login.driver.find_element_by_id('EndInterval')).select_by_visible_text('下午')
        time.sleep(1)
        self.login.driver.find_element_by_id('Duration').clear()
        time.sleep(1)
        self.login.driver.find_element_by_id('Duration').send_keys('1')
        time.sleep(1)
        self.login.driver.find_element_by_id('Content').send_keys('身体不适，需要请假一天')
        time.sleep(1)
        f1 = self.login.driver.find_element_by_xpath("//span[contains(@class,'glyphicon glyphicon-plus-sign')]").click()
        time.sleep(1)
        UploadFile().upload_file(f1, r'C:\Users\zheng\Desktop\图片\微信截图_20200515104338.png')
        time.sleep(3)
        self.login.driver.find_element_by_id('btn_sub').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        print('提交请假申请成功')
        time.sleep(3)

    def edit_my_leave(self):
        self.login.driver.find_element_by_xpath('//tr[1]//td[2]//a[1]//span[1]').click()
        time.sleep(2)
        self.login.driver.find_element_by_id('Content').clear()
        time.sleep(1)
        self.login.driver.find_element_by_id('Content').send_keys('修改后的请假事由')
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_sub').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        print('修改请假申请成功')
        time.sleep(3)

    def revoke_my_leave(self):
        self.login.driver.find_element_by_xpath('//tr[1]//td[2]//a[2]//span[1]').click()
        time.sleep(2)
        try:
            if self.login.driver.find_element_by_xpath(
                    '/html[1]/body[1]/div[2]/div[2]/div[1]/div[2]/div[2]/table[1]/tbody[1]/tr[1]/td[8]').text == '已撤销':
                print('请假申请撤销成功')
            else:
                print('未撤销成功')
        except:
            print('未撤销成功，报异常')
        self.login.driver.close()

