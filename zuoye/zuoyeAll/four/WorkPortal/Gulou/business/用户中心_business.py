
from time import sleep

import pywinauto
from pywinauto.keyboard import send_keys

# from Gulou.business.登录_business import Login
# from Gulou.business.首页_business import Home
# from Gulou.config.browser import Browser
import time

from zuoye.zuoyeAll.four.WorkPortal.Gulou.business.登录_business import Login
from zuoye.zuoyeAll.four.WorkPortal.Gulou.business.首页_business import Home
from zuoye.zuoyeAll.four.WorkPortal.Gulou.config.browser import Browser

date = str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
date6 = str(time.strftime('%Y%m',time.localtime(time.time())))
date2 = str(time.strftime('%M%S',time.localtime(time.time())))





class UserCenter:
    def __init__(self, browser):
        self.browser = browser


    # 用户管理，新增
    def user_management_click(self):
        self.browser.driver.implicitly_wait(5)
        print("用户中心，用户管理，进入 ： $ ")
        sleep(2)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'用户管理')]").click()  # 用户管理
        sleep(2)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'系统用户')]").click()  # 系统用户

    def user_management_add(self):
        self.browser.driver.implicitly_wait(5)
        print("---------------------------------------------")
        print("用户中心，用户管理，新增 ： $ ")
        sleep(2)
        self.user_management_click()  #进入 用户管理
        global username
        username = "add" + date2
        phone_no = "15988" + date6
        full_name =  "张" + date6
        ID = "110101198801010019"
        role = "平台管理员"
        sleep(2)
        self.browser.driver.find_element_by_xpath("//button/span[contains(text(),'新增')]").click()  #新增
        sleep(2)
        self.browser.driver.find_element_by_xpath(
            "//*[contains(text(),'所属区域')]/following-sibling::*//button").click()  # 点击所属区域后的按钮
        sleep(2)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'徐州市鼓楼区')]/../label/span").click()  # 勾选徐州市鼓楼区
        sleep(2)
        self.browser.driver.find_element_by_xpath(
            "//div[contains(@aria-label,'新增平台用户')]//span[contains(text(),'确定')]").click()  # 确认
        sleep(2)
        self.browser.driver.find_element_by_xpath("//*[contains(text(),'平台角色')]/following-sibling::*//div[1]/input").send_keys(role) #角色
        sleep(2)
        self.browser.driver.find_element_by_xpath("//ul/li[1]/span[contains(text(),'{}')]".format(role)).click()  #确认
        sleep(2)
        self.browser.driver.find_element_by_xpath("//*[contains(text(),'登录名')]/following-sibling::*//input").send_keys(username)
        self.browser.driver.find_element_by_xpath("//*[contains(text(),'姓名')]/following-sibling::*//input").send_keys(full_name)
        self.browser.driver.find_element_by_xpath("//*[contains(text(),'手机号')]/following-sibling::*//input").send_keys(phone_no)
        self.browser.driver.find_element_by_xpath("//*[contains(text(),'身份证号')]/following-sibling::*//input").click()
        self.browser.driver.find_element_by_xpath("//*[contains(text(),'身份证号')]/following-sibling::*//input").send_keys(ID)
        sleep(2)

        self.browser.driver.find_element_by_xpath("//*[contains(text(),'所属部门')]/following-sibling::*//input").click()
        sleep(2)
        self.browser.driver.find_elements_by_xpath("//div/ul/li/span[contains(text(),'区司法局')]")[1].click()  #区司法局
        sleep(2)
        self.browser.driver.find_element_by_xpath("//form/div[8]/div/div/div/img").click() #头像上传
        sleep(2)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'点击，或拖动图片至此处')]").click() #上传图片
        sleep(2)
        """上传文件"""
        win1 = pywinauto.Desktop()
        sleep(1)
        bow1 = win1['打开']
        sleep(1)
        bow1["文件名(&N):Edit"].type_keys(r"E:\0.jpg")
        sleep(2)
        send_keys("{VK_RETURN}")
        sleep(2)
        """上传文件"""
        self.browser.driver.find_element_by_xpath("//a[contains(text(),'保存')]").click()  #图片保存
        sleep(2)
        self.browser.driver.find_element_by_xpath("//a[contains(text(),'关闭')]").click()  #关闭
        sleep(2)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'确认')]").click()  #确认
        sleep(2)
        try:
            sleep(1)
            self.browser.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]")
        except:
            print("新增失败***！！！，用户名：" + str(username))
            return False
        else:
            print("新增成功，用户名：" + str(username))
            return False

    def user_management_search(self,serach):
        self.browser.driver.implicitly_wait(5)
        sleep(2)
        print("---------------------------------------------")
        print("用户中心，用户管理，查询 ： $ ")
        global username
        self.browser.driver.find_element_by_xpath("//input[contains(@placeholder,'请输入登录名、姓名、手机号或身份证号')]").clear()
        sleep(2)
        self.browser.driver.find_element_by_xpath("//input[contains(@placeholder,'请输入登录名、姓名、手机号或身份证号')]").send_keys(serach)
        sleep(2)
        self.browser.driver.find_element_by_xpath("//button/span[contains(text(),'查询')]").click()
        sleep(2)
        try:
            self.browser.driver.find_element_by_xpath("//div[4]//div[2]//table[1]//tbody[1]//tr[1]//td[3]//div[1][contains(text(),'{}')]".format(serach))
            sleep(2)
        except:
            print("没有查询到用户***！！！，登录名：" + str(serach))
            return False
        else:
            print("查询成功，登录名：" + str(serach))
            return True

    def user_management_edit(self):  #结尾调用的是user_management_search  ； 已返回结果
        self.browser.driver.implicitly_wait(5)
        sleep(2)
        print("---------------------------------------------")
        print("用户中心，用户管理，编辑 ： $ ")
        global username,username_edit
        self.user_management_search(username)
        username_edit = "edit" + date2
        self.browser.driver.find_elements_by_xpath("//button[2]/span[contains(text(),'编辑')]")[2].click()
        sleep(2)
        self.browser.driver.find_element_by_xpath("//*[contains(text(),'登录名')]/following-sibling::*//input").clear()
        sleep(2)
        self.browser.driver.find_element_by_xpath("//*[contains(text(),'登录名')]/following-sibling::*//input").send_keys(username_edit)
        sleep(2)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'确认')]").click()  # 确认
        sleep(2)
        self.user_management_search(username_edit)

    def new_user_login(self):  #结尾 调用的是 login；login中已返回 T  F
        self.browser.driver.implicitly_wait(5)
        sleep(2)
        print("---------------------------------------------")
        print("当前用户推出，新增加的用户登录验证 ： $ ")
        global username,username_edit
        self.browser.driver.find_element_by_xpath("//img[@class = 'user-avatar']").click() #点击用户
        sleep(2)
        self.browser.driver.find_element_by_xpath("//li[contains(text(),'退出登录')]").click()  #退出登录
        sleep(2)
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[3].click()
        sleep(10)
        Login(self.browser).login(username_edit,"GLabc123")

    def user_management_delete(self):   #删除新建的数据  结尾调用 user_management_search_delete 已反馈结果 T  F
        self.browser.driver.implicitly_wait(5)
        sleep(2)
        print("---------------------------------------------")
        print("用户中心，用户管理，编辑 ： $ ")
        self.user_management_click()  #进入 用户管理
        global  username_edit
        self.user_management_search(username_edit)
        sleep(2)
        self.browser.driver.find_elements_by_xpath("//button[4]/span[contains(text(),'删除')]")[2].click()
        sleep(2)
        self.browser.driver.find_elements_by_xpath("//button[2]/span[contains(text(),'确定')]")[1].click()  #确认
        sleep(2)
        self.user_management_search_delete(username_edit)

    def user_management_search_delete(self,serach):
        self.browser.driver.implicitly_wait(5)
        sleep(2)
        print("---------------------------------------------")
        print("用户中心，用户管理，查询 ： $ ")
        global username
        self.browser.driver.find_element_by_xpath("//input[contains(@placeholder,'请输入登录名、姓名、手机号或身份证号')]").clear()
        sleep(2)
        self.browser.driver.find_element_by_xpath("//input[contains(@placeholder,'请输入登录名、姓名、手机号或身份证号')]").send_keys(serach)
        sleep(2)
        self.browser.driver.find_element_by_xpath("//button/span[contains(text(),'查询')]").click()
        sleep(2)
        try:
            self.browser.driver.find_element_by_xpath("//div[4]//div[2]//table[1]//tbody[1]//tr[1]//td[3]//div[1][contains(text(),'{}')]".format(serach))
            sleep(2)
        except:
            print("删除成功，登录名：" + str(serach))
            return True
        else:
            print("删除失败***！！！，登录名：" + str(serach))
            return False





if __name__ == '__main__':
    br = Browser("http://192.168.20.243:9083")
    br.browser()
    Login(br).login("jswq168","xsw2CDE#168")
    Home(br).system_open("用户中心","首页 - 智慧鼓楼工作门户")
    UserCenter(br).user_management_add()
    # br.driver.close()



