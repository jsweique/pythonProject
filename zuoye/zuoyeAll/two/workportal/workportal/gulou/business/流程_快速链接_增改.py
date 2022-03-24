import os
import time


class Quicklinks:
    def __init__(self,login):
        self.login = login

    def add_quick_links(self,name):
        time.sleep(3)
        self.login.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/div[2]').click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]').click()
        time.sleep(2)
        # name1 = '百度一下'
        # s = str(self.login.random.randint(1000, 9000))
        # name = name1 + s
        id = 'https://www.baidu.com/'
        self.login.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[7]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys(name)
        time.sleep(3)
        self.login.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[7]/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/input[1]').send_keys(id)
        time.sleep(3)
        self.login.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[7]/div[1]/div[3]/div[1]/button[1]').click()
        time.sleep(3)
        f = self.login.driver.find_element_by_xpath('//a[contains(text(),"{}")]'.format(name)).text
        print('获取到的快速链接名称：{}'.format(f))
        time.sleep(2)


    # def click_quick_links(self):
    #     time.sleep(3)
    #     global name,title1,title2
    #     title1 = '个人工作台 - 智慧鼓楼工作门户'
    #     title2 = '百度一下，你就知道'
    #     self.login.driver.find_element_by_link_text(name).click()
    #     self.login.driver.swicth_windows(title2)
    #     time.sleep(2)
    #     print("切换页面的title是：" + self.login.driver.title)
    #     self.login.driver.find_element_by_xpath("//input[@id='kw']").send_keys('12345')
    #     time.sleep(3)
    #     self.login.driver.find_element_by_id('su').click()
    #     time.sleep(3)

    def edit_quick_links(self,name):
        name2 = '百度一下'
        self.login.driver.find_element_by_xpath('//a[contains(text(),"{}")]/following::div[1]'.format(name)).click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[7]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]').clear()
        time.sleep(2)
        self.login.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[7]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys(name2)
        time.sleep(3)
        self.login.driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[7]/div[1]/div[3]/div[1]/button[1]').click()
        time.sleep(2)
        try:
            ff = self.login.driver.find_element_by_xpath('/html[1]/body[1]/div[2]/p[1]').text
            if ff == '修改成功':
                print('快速链接名称编辑成功')
            else:
                print('名称编辑失败！！')
        except:
            print('未获取编辑的提示')
        time.sleep(2)

    def delete_quick_links(self,name):
        self.login.driver.find_element_by_xpath('//a[contains(text(),"{}")]/following::div[1]'.format(name)).click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath('//span[contains(text(),"删除")]').click()
        time.sleep(2)
        self.login.driver.find_element_by_xpath('//span[contains(text(),"确定")]').click()
        time.sleep(2)
        try:
            fff = self.login.driver.find_element_by_xpath('//P[contains(text(),"删除成功")]').text
            if fff == '删除成功':
                print('快速链接删除成功')
            else:
                print('删除失败！')
        except:
            print('未获取到删除的提示')
        time.sleep(3)
