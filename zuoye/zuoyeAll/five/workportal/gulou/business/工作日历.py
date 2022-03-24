import random
import time


class ShopCalendar:
    def __init__(self, login):
        self.login = login

    def add_shopCalendar(self, num):
        time.sleep(1)
        self.login.driver.find_element_by_xpath(
            "//body/div[@id='app']/div[contains(@class,'pages')]/div[contains(@class,'UserCenter')]/div[contains(@class,'mt20 el-row is-justify-space-around el-row--flex')]/div[contains(@class,'workDay el-col el-col-8')]/div[contains(@class,'myCalendar fc fc-media-screen fc-direction-ltr fc-theme-standard')]/div[contains(@class,'fc-view-harness fc-view-harness-active')]/div[contains(@class,'fc-daygrid fc-dayGridMonth-view fc-view')]/table[contains(@class,'fc-scrollgrid-liquid')]/tbody/tr[contains(@class,'fc-scrollgrid-section-liquid')]/td/div[contains(@class,'fc-scroller-harness fc-scroller-harness-liquid')]/div[contains(@class,'fc-scroller fc-scroller-liquid-absolute')]/div[contains(@class,'fc-daygrid-body fc-daygrid-body-unbalanced')]/table[contains(@class,'fc-scrollgrid-sync-table')]/tbody/tr[1]/td[2]/div[1]/div[1]").click()
        time.sleep(2)
        # CSS元素定位
        self.login.driver.find_elements_by_css_selector('span.el-radio-button__inner')[1].click()
        time.sleep(1)
        # name = '这是填写的事件标题{}'.format(random.randint(1, 20))
        # class_name元素定位
        self.login.driver.find_elements_by_class_name('el-input__inner')[2].send_keys(num)
        time.sleep(2)
        # xpath相对路径
        self.login.driver.find_element_by_xpath("//textarea[@placeholder='请输入事件描述']").send_keys('事件描述')
        time.sleep(2)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-dialog__wrapper')]//div[3]//div[1]//button[1]").click()
        time.sleep(2)
        # xpath绝对路径
        t = self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[2]/div[1]/a[1]/div[3]").text
        print('获取到的工作日历名称是：{}'.format(num))
        time.sleep(2)

    def edit_shopCalendar(self, nu):
        self.login.driver.find_elements_by_xpath("//div[contains(text(),'{}')]".format(nu))[0].click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//textarea[@placeholder='请输入事件描述']").clear()
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//textarea[@placeholder='请输入事件描述']").send_keys('编辑时填写的内容')
        time.sleep(1)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-dialog__wrapper')]//div[3]//div[1]//button[1]").click()
        time.sleep(2)
        try:
            tt = self.login.driver.find_element_by_xpath('//p[contains(text(),"修改成功")]').text
            if tt == '修改成功':
                print('工作日历编辑成功')
            else:
                print('编辑失败！！')
        except:
            print('未获取编辑的提示')
        time.sleep(1)

    def delete_shopCalendar(self,nu):
        self.login.driver.find_elements_by_xpath("//div[contains(text(),'{}')]".format(nu))[0].click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-dialog__wrapper')]//div[3]//div[1]//button[3]").click()
        time.sleep(1)
        self.login.driver.find_element_by_xpath(
            "//button[contains(@class,'el-button el-button--default el-button--small el-button--primary')]").click()
        time.sleep(2)
        try:
            self.login.driver.find_element_by_xpath('//p[contains(text(),"删除成功")]')
            # if ttt == '删除成功':
            #     print('工作日历删除成功')
            # else:
            #     print('删除失败！！')
        except:
            print('未获取到删除的提示')
        else:
            print('工作日历删除成功')
        time.sleep(1)
