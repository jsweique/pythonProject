import time
from time import sleep

date = str(time.strftime('%S%M',time.localtime(time.time())))

class Role:
    #登录
    def __init__(self, browser, sys_name):
        self.browser = browser
        self.sys_name = sys_name

    #进入角色页
    def switch_Menu (self):
        self.browser.driver.implicitly_wait(5)

        self.browser.driver.find_elements_by_class_name("el-carousel__button")[1].click() #我的应用翻页
        sleep(3)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'"+self.sys_name+"')]").click()#选择用户中心
        sleep(3)
        self.browser.driver.switch_to.window( self.browser.driver.window_handles[-1]) #切换窗口
        sleep(2)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'角色管理')]").click()#选择菜单
        sleep(2)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'平台角色')]").click()
        sleep(5)


    #新增角色
    def role_Add(self):
        self.browser.driver.implicitly_wait(5)

        self.browser.driver.find_element_by_xpath("//span[contains(text(),'新增')]").click()#点击新增
        sleep(2)
        role_title = date + "自动化测试角色"
        self.browser.driver.find_elements_by_xpath("//input[@placeholder='角色名称']")[1].send_keys(role_title)#输入角色名
        sleep(1)
        self.browser.driver.find_element_by_xpath("//input[@placeholder='角色行政级别']").click()#点击选择行政级别
        sleep(2)
        self.browser.driver.find_element_by_xpath("//div[@x-placement='bottom-start']/descendant::*/span[contains(text(),'网格')]").click()
        sleep(2)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'确认')]").click()#点击确认
        sleep(2)
        try:
            self.browser.driver.find_element_by_xpath("//p[@class='el-message__content']")  # 获取保存成功
            print('新增角色成功，名称为：{}'.format(role_title))
            sleep(1)
            print("--------------------------------------------------------------------------------")
            sleep(1)
        except:
            print('新增角色失败')
            sleep(1)
            print("--------------------------------------------------------------------------------")
            sleep(1)
            return False
        sleep(1)
        self.browser.driver.find_element_by_xpath("//input[@placeholder='角色名称']").send_keys(role_title)  # 按名称搜索
        sleep(2)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'查询')]").click()  # 点击查询
        sleep(5)


    #编辑角色
    def role_Edit(self):
        self.browser.driver.implicitly_wait(5)

        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'编辑')]")[2].click()#点击编辑
        sleep(2)
        self.browser.driver.find_elements_by_xpath("//input[@placeholder='角色名称']")[1].clear()#清除标题填写新内容
        sleep(2)
        role_title = date + "修改角色名称"
        self.browser.driver.find_elements_by_xpath("//input[@placeholder='角色名称']")[1].send_keys(role_title)
        sleep(2)
        self.browser.driver.find_element_by_tag_name("textarea").send_keys("测试修改角色")#增加备注
        sleep(2)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'确认')]").click()#确定
        sleep(1)
        try:
            self.browser.driver.find_element_by_xpath("//p[@class='el-message__content']")  # 获取保存成功
            print('修改角色成功，名称为：{}'.format(role_title))
            sleep(1)
            print("--------------------------------------------------------------------------------")
            sleep(1)
        except:
            print('修改角色失败')
            sleep(1)
            print("--------------------------------------------------------------------------------")
            sleep(1)
            return False

        sleep(1)
        self.browser.driver.find_element_by_xpath("//input[@placeholder='角色名称']").clear()  # 查询修改后的标题
        sleep(2)
        self.browser.driver.find_element_by_xpath("//input[@placeholder='角色名称']").send_keys(role_title)
        sleep(2)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'查询')]").click()
        sleep(5)

    #菜单授权
    def role_Authorize_menu(self):
        self.browser.driver.implicitly_wait(5)

        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'菜单授权')]")[3].click() #选择菜单授权
        sleep(5)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'门户管理')]/../label/span").click()#勾选门户管理
        sleep(3)
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[2].click()
        sleep(1)
        try:
            self.browser.driver.find_element_by_xpath("//p[@class='el-message__content']")  # 获取保存成功
            sleep(5)
            print('菜单授权成功，授权的菜单为：{}'.format("门户管理"))
            sleep(1)
            print("--------------------------------------------------------------------------------")
        except:
            print('菜单授权失败')
            sleep(1)
            print("--------------------------------------------------------------------------------")
            return False
        else:
            return True


    #大屏导航授权
    def role_Authorize_screen(self):
        self.browser.driver.implicitly_wait(5)

        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'大屏导航授权')]")[2].click() # 选择大屏导航授权
        sleep(5)
        self.browser.driver.find_element_by_xpath("// input[contains( @ placeholder, '请输入导航名称')]").send_keys("公共管理") #查询导航
        sleep(5)
        self.browser.driver.find_elements_by_xpath("//i[@class='el-icon-search']")[1].click()#点击查询
        sleep(5)
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'公共管理')]/../../label/span/span")[1].click()#选择第二个
        sleep(3)
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[3].click()
        sleep(1)
        try:
            self.browser.driver.find_element_by_xpath("//p[@class='el-message__content']")  # 获取保存成功
            sleep(5)
            print('大屏导航授权成功，授权的导航为：{}'.format("公共管理"))
            sleep(1)
            print("--------------------------------------------------------------------------------")
        except:
            print('大屏导航授权失败')
            sleep(1)
            print("--------------------------------------------------------------------------------")
            return False
        else:
            return True

    #APP导航授权
    def role_Authorize_app(self):
        self.browser.driver.implicitly_wait(5)

        self.browser.driver.find_element_by_xpath("//div[contains(@class,'el-table__fixed-right')]//span[contains(text(),'app')]").click() #点击APP授权
        sleep(5)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'预约单')]/../label/span").click() #点击预约单
        sleep(3)
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[1].click()
        sleep(1)
        try:
            self.browser.driver.find_element_by_xpath("//p[@class='el-message__content']")  # 获取保存成功
            sleep(5)
            print('APP导航授权成功，授权的导航为：{}'.format("预约单"))
            sleep(1)
            print("--------------------------------------------------------------------------------")
        except:
            print('APP导航授权失败')
            sleep(1)
            print("--------------------------------------------------------------------------------")
            return False
        else:
            return True


    #应用配置授权
    def role_Authorize_sys(self):
        self.browser.driver.implicitly_wait(5)

        self.browser.driver.find_element_by_xpath("//div[contains(@class,'el-table__fixed-right')]//button[4]//span[1]").click()#应用配置授权
        sleep(5)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'社会治理')]/../label/span").click()#勾选社会治理
        sleep(3)
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[4].click()
        sleep(1)
        try:
            self.browser.driver.find_element_by_xpath("//p[@class='el-message__content']")  # 获取保存成功
            sleep(5)
            print('应用配置授权成功，授权的应用为：{}'.format("社会治理"))
            sleep(1)
            print("--------------------------------------------------------------------------------")
        except:
            print('应用配置授权失败')
            sleep(1)
            print("--------------------------------------------------------------------------------")
            return False
        else:
            return True


    #角色删除（需要取消所有的授权）
    def role_Delete(self):
        self.browser.driver.implicitly_wait(5)

        #【步骤同上】取消已授权的菜单
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'菜单授权')]")[3].click()
        sleep(5)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'门户管理')]/../label/span").click()
        sleep(3)
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[2].click()
        sleep(5)
        # 【步骤同上】取消已授权的大屏导航
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'大屏导航授权')]")[2].click()
        sleep(5)
        self.browser.driver.find_element_by_xpath("// input[contains( @ placeholder, '请输入导航名称')]").send_keys("公共管理")
        sleep(5)
        self.browser.driver.find_elements_by_xpath("//i[@class='el-icon-search']")[1].click()
        sleep(5)
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'公共管理')]/../../label/span/span")[1].click()
        sleep(3)
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[3].click()
        sleep(5)
        #【步骤同上】取消APP授权
        self.browser.driver.find_element_by_xpath("//div[contains(@class,'el-table__fixed-right')]//span[contains(text(),'app')]").click()
        sleep(5)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'预约单')]/../label/span").click()
        sleep(3)
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[1].click()
        sleep(5)
        #【步骤同上】取消应用授权
        self.browser.driver.find_element_by_xpath("//div[contains(@class,'el-table__fixed-right')]//button[4]//span[1]").click()
        sleep(5)
        self.browser.driver.find_element_by_xpath("//span[contains(text(),'社会治理')]/../label/span").click()
        sleep(3)
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[4].click()
        sleep(5)

        #点击删除
        self.browser.driver.find_element_by_xpath("//div[contains(@class,'el-table__fixed-right')]//button[7]//span[1]").click()
        sleep(5)
        self.browser.driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[1].click()
        sleep(1)
        try:
            self.browser.driver.find_element_by_xpath("//p[contains(text(),'删除成功')]")  # 获取删除成功
            print("删除角色成功")
            sleep(1)
            print("--------------------------------------------------------------------------------")
            sleep(1)
            self.browser.driver.switch_to.window(self.browser.driver.window_handles[0])  # 切换回首页
        except:
            print('删除角色失败')
            sleep(1)
            print("--------------------------------------------------------------------------------")
            sleep(1)
            self.browser.driver.switch_to.window(self.browser.driver.window_handles[0])  # 切换回首页
            return False
        else:
            return True

