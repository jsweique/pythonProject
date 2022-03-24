import time

from selenium.webdriver.support import select
from 文件上传 import UploadFile


class Element:
    def __init__(self, login):
        self.login = login

    def add_element(self):
        self.login.driver.find_element_by_link_text('后台数据管理控制台').click()
        time.sleep(3)
        self.login.driver.find_element_by_link_text('网格资源库').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('地').click()
        time.sleep(1)
        self.login.driver.find_element_by_link_text('房屋信息登记').click()
        time.sleep(2)
        frame = self.login.driver.find_element_by_xpath('//*[@id="tt"]/div[2]/div[2]/div/iframe')  # 切换iframe
        self.login.driver.switch_to.frame(frame)
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_create').click()  # 新增
        time.sleep(2)
        # self.login.driver.switch_to.default_content()
        frame = self.login.driver.find_element_by_xpath('/html/body/div[10]/div[2]/iframe')  # 切换iframe
        self.login.driver.switch_to.frame(frame)
        self.login.driver.find_element_by_id('name').send_keys('测试')
        time.sleep(3)
        self.login.driver.find_element_by_id('SingleLine19').send_keys('320309196601020304')
        time.sleep(1)
        select.Select(self.login.driver.find_element_by_id('DropdownList10')).select_by_value('商住房')
        time.sleep(1)
        self.login.driver.find_element_by_id('memo').send_keys('5')
        time.sleep(1)
        self.login.driver.find_element_by_id('addr').send_keys('30平方')
        time.sleep(1)
        self.login.driver.find_element_by_id('SingleLine17').send_keys('ABC123')
        time.sleep(1)
        self.login.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')  # 滑动到底部
        time.sleep(1)
        self.login.driver.find_element_by_id('SingleLine20').send_keys('15100022336')
        time.sleep(1)
        self.login.driver.find_element_by_id('SingleLine21').send_keys('王五')
        time.sleep(1)
        self.login.driver.find_element_by_id('SingleLine26').send_keys('3203061955')
        time.sleep(1)
        f1 = self.login.driver.find_element_by_xpath("//img[@id='c']").click()  # 上传图片
        # time.sleep(3)
        UploadFile().upload_file(f1, r'C:\Users\zheng\Desktop\图片\微信截图_20200515104338.png')
        time.sleep(2)
        self.login.driver.find_element_by_id('btn_setMap').click()  # 定位
        time.sleep(2)
        self.login.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(1)
        select.Select(self.login.driver.find_element_by_xpath("//select[@id='department_2']")).select_by_visible_text(
            r'徐州市沛县/安国镇/')
        time.sleep(1)
        select.Select(self.login.driver.find_element_by_xpath("//select[@id='department_1']")).select_by_visible_text(
            '袁庄居')
        time.sleep(1)
        select.Select(self.login.driver.find_element_by_xpath("//select[@id='department_0']")).select_by_visible_text(
            '袁庄居自然网格1')
        time.sleep(1)
        self.login.driver.find_element_by_id('btn_showArea').click()  # 选定网格
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//div[@class='row mt10']//option[9]").click()  # 选择标准地址
        time.sleep(1)
        self.login.driver.find_element_by_xpath(
            "//button[contains(@class,'btn btn-success btn-block btn_sub')]").click()  # 提交
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()  # 确定提交
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()  # 提交结果
        time.sleep(5)
