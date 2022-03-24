import datetime
import random
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from 文件上传 import UploadFile


class EventAdd:
    def __init__(self, login):
        self.login = login

    def event_add(self):
        self.login.driver.find_element_by_xpath(r'/html/body/div/div[2]/section/div[1]/div/div[17]').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('后台数据管理控制台').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="grandpa"]/li/ul/li[4]').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="grandpa"]/li/ul/li[4]/ul/li[1]').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath('//*[@id="grandpa"]/li/ul/li[4]/ul/li[1]/ul/li[2]').click()
        time.sleep(1)
        frame = self.login.driver.find_element_by_xpath('//*[@id="tt"]/div[2]/div[2]/div/iframe')
        self.login.driver.switch_to.frame(frame)
        time.sleep(2)
        self.login.driver.find_element_by_id('btn_create').click()
        time.sleep(3)

        # self.login.switch_to.frame(self.login.find_element_by_xpath('//*[@id="tt"]/div[2]/div[2]/div/iframe'))
        name = str(datetime.date.today()) + '日上报的随机事件：' + str(random.randint(1, 100))
        self.login.driver.find_element_by_id('EnumEventProcType').click()
        time.sleep(1)
        Select(self.login.driver.find_element_by_id('EnumEventProcType')).select_by_value('2')
        time.sleep(1)
        self.login.driver.find_element_by_id('name').send_keys(name)
        time.sleep(1)
        self.login.driver.find_element_by_id('memo').send_keys('出租用房的消防审验，在排查人员基础信息的同时，和出租房业主讲解，消防安全有关知识。')
        time.sleep(1)
        self.login.driver.find_element_by_id('addr').send_keys('江苏省徐州市沛县陈平路')
        time.sleep(1)

        f1 = self.login.driver.find_element_by_xpath("//a[@class='uploadImg SinglePic']//img").click()  # 上传图片
        time.sleep(1)
        UploadFile().upload_file(f1, r'C:\Users\zheng\Desktop\图片\微信截图_20200515104338.png')  # 调用上传文件函数
        time.sleep(5)
        # f1 = self.login.driver.find_element_by_xpath("//i[@class='glyphicon glyphicon-hd-video']").click()  # 上传视频
        # time.sleep(1)
        # UploadFile().upload_file(f1, r'C:\Users\zheng\Desktop\视频\1.mp4')
        # self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        # time.sleep(3)

        self.login.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')#滑动到底部
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_setMap').click()
        time.sleep(2)
        self.login.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(1)
        Select(self.login.driver.find_element_by_id('department_2')).select_by_visible_text('徐州市沛县/沛城街道/')
        time.sleep(1)
        Select(self.login.driver.find_element_by_id('department_1')).select_by_visible_text('新风居')
        time.sleep(1)
        Select(self.login.driver.find_element_by_id('department_0')).select_by_visible_text('新风网格1')
        time.sleep(1)

        self.login.driver.find_element_by_id('btn_showArea').click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//*[name()='path' and contains(@stroke-linejoin,'round')]").click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/button').click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
        time.sleep(1)
        code = self.login.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
        name = self.login.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text
        return code, name

# d = webdriver.Chrome
# d.find_element_by_class_name('cover').send_keys(r'C:\Users\zheng\Desktop\图片\3801213fb80e7bec05b9f84614d59c3f9a506b3c.jpeg')
# d.find_element_by_xpath().text
