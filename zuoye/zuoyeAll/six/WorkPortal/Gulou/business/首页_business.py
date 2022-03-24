import os
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from Gulou.business.登录_business import Login
from Gulou.config.browser import Browser
import time
date = str(time.strftime('%S%M',time.localtime(time.time())))


class Home:

    def __init__(self, browser):
        self.browser = browser

    # 快速链接 新增
    def quick_links_add(self):
        self.browser.driver.implicitly_wait(10)
        for i in range(2):
            sleep(2)
            print("首页，快速链接,新增 ： $ ")
            global  name
            name = "百度百科"  + str(i)
            addr = "https://baike.baidu.com/"
            self.browser.driver.implicitly_wait(10)
            sleep(2)
            try:
                button_kslj = self.browser.driver.find_element_by_xpath('//div[contains(text(),"快速链接")]')
            except:
                print("首页——快速链接 未找到***！！！")
                sleep(1)
                print("--------------------------------------------------------------------------------")
                self.browser.driver.close()
                os._exit(0)
                return False
            else:
                button_kslj.click()
            sleep(5)
            self.browser.driver.find_element_by_xpath('//div[contains(text(),"添加")]').click()
            sleep(2)
            self.browser.driver.find_element_by_xpath('//label[contains(text(),"快捷名称")]/following-sibling::*//input').send_keys(name)
            sleep(2)
            self.browser.driver.find_element_by_xpath('//label[contains(text(),"链接地址")]/following-sibling::*//input').send_keys(addr)
            sleep(2)
            self.browser.driver.find_element_by_css_selector('div.pages div.el-dialog__wrapper:nth-child(7) div.el-dialog div.el-dialog__footer \
            div.dialog-footer button.el-button.filter-item.el-button--primary.el-button--small:nth-child(1) > span:nth-child(1)').click()
            sleep(5)
            try:
                self.browser.driver.find_element_by_xpath('//a[contains(text(),"{}")]'.format(name))
                sleep(2)
            except:
                print("首页，新增 快速链接 失败***！！！")
                sleep(1)
                print("--------------------------------------------------------------------------------")
                self.browser.driver.close()
                os._exit(0)
                return False
            else:
                print("首页，新增 快速链接 成功，名称：" + str(name))
                sleep(1)
                print("--------------------------------------------------------------------------------")
                # return True

    # 快速链接点击，跳转
    def quick_links_click(self):
        self.browser.driver.implicitly_wait(5)
        sleep(2)
        print("首页，快速链接,验证链接 ： $ ")
        title2 = '百度百科_全球领先的中文百科全书'
        self.browser.driver.find_element_by_link_text('百度百科0').click()
        sleep(2)
        # 切换至新的 窗口
        self.browser.switch_windows5(title2)  #切换到 title2
        sleep(3)
        print("切换页面的title是：" + self.browser.driver.title)   #打印 title
        self.browser.driver.find_element_by_id('query').send_keys("12345")
        sleep(2)
        self.browser.driver.find_element_by_id('search').click()
        sleep(2)
        self.browser.driver.close()  #关闭当前窗口
        sleep(2)
        self.browser.driver.switch_to.window(self.browser.driver.window_handles[0])  #切换至第一个窗口
        sleep(3)

    # 编辑快速链接
    def quick_links_edit(self):
        self.browser.driver.implicitly_wait(5)
        sleep(2)
        name_edit = "编辑百科"  + date
        print("首页，快速链接,编辑 ： $ ")
        self.browser.driver.find_element_by_xpath('//a[contains(text(),"{}")]/following::div[1]'.format('百度百科0')).click()
        sleep(2)
        self.browser.driver.find_element_by_xpath('//label[contains(text(),"快捷名称")]/following-sibling::*//input').clear()
        sleep(2)
        self.browser.driver.find_element_by_xpath('//label[contains(text(),"快捷名称")]/following-sibling::*//input').send_keys(name_edit)
        sleep(2)
        self.browser.driver.find_elements_by_xpath('//span[contains(text(),"保存")]')[1].click()
        sleep(3)
        try:
            self.browser.driver.find_element_by_xpath('//a[contains(text(),"{}")]'.format(name_edit))
            sleep(2)
        except:
            print("首页，编辑 快速链接 失败***！！！")
            sleep(1)
            print("--------------------------------------------------------------------------------")
            self.browser.driver.close()
            os._exit(0)
            return False
        else:
            print("首页，编辑 快速链接 成功，名称：" + str(name_edit))
            sleep(1)
            print("--------------------------------------------------------------------------------")
            return True

    # 删除快速链接
    def quick_links_delete(self):
        self.browser.driver.implicitly_wait(5)
        sleep(2)
        print("首页，快速链接,验证链接 ： $ ")
        try:
            button = self.browser.driver.find_element_by_xpath('//a[contains(text(),"{}")]/following::div[1]'.format('百度百科1'))
            sleep(2)
        except:
            print("首页，未找到快速链接***！！！")
            sleep(1)
            print("--------------------------------------------------------------------------------")
            self.browser.driver.close()
            os._exit(0)
            return False
        else:
            button.click()
        sleep(3)
        self.browser.driver.find_element_by_xpath('//span[contains(text(),"删除")]').click()
        sleep(2)
        self.browser.driver.find_element_by_xpath('//span[contains(text(),"确定")]').click()
        try:
            sleep(1)
            self.browser.driver.find_element_by_xpath('//P[contains(text(),"删除成功")]')
        except:
            print("首页，删除 快速链接 失败***！！！")
            sleep(1)
            print("--------------------------------------------------------------------------------")
            self.browser.driver.close()
            os._exit(0)
            return False
        else:
            print("首页，删除 快速链接 成功")
            sleep(1)
            print("--------------------------------------------------------------------------------")
            return True

    # 点击系统名称，确认系统标题  system_name 系统名称  title_name  标题
    def system_open(self,system_name,title_name):
        self.browser.driver.implicitly_wait(5)
        sleep(2)
        print("首页，点击应用中心 ： $ ")
        self.browser.driver.find_element_by_xpath("//li[contains(text(),'应用中心')]").click()
        sleep(2)
        # name = self.browser.driver.find_elements_by_xpath('//*[@id="app"]/div/div/div/div/div/h4')
        # for i in name:
        #     print(i.text)
        #
        # print(len(name))
        self.browser.driver.find_elements_by_xpath('//*[contains(text(),"{}")]'.format(system_name))[0].click()  #此处标准用复数
        sleep(2)
        self.browser.driver.find_elements_by_xpath('//*[contains(text(),"网格化")]')[0].click()  #此处用复数
        sleep(2)
        self.browser.driver.find_elements_by_xpath('//*[contains(text(),"编办1+4")]')[0].click()  #此处用复数
        sleep(5)
        self.browser.switch_windows5(title_name)     #切换到用户中心
        sleep(5)



if __name__ == '__main__':
    br = Browser("http://192.168.20.243:9083")
    br.browser()
    Login(br).login("jswq168","xsw2CDE#168")
    Home(br).system_open("用户中心","首页 - 智慧鼓楼工作门户")

    br.driver.close()







