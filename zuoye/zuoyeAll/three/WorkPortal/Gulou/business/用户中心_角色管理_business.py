from time import sleep
import time

class Role:
    def __init__(self, login):
        self.login = login

    def switch_window(self):
        # 切换窗口
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/ul[1]/li[2]/button[1]").click() #选中第二个滚动条
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'用户中心')]").click() #选中用户中心
        time.sleep(2)
        self.login.driver.switch_to.window(self.login.driver.window_handles[-1])
        time.sleep(2)

    def switch_menu(self):
        # 进入角色管理
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/div[5]/li[1]/div[1]/span[1]").click()  # 找到角色管理
        time.sleep(2)
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/div[5]/li[1]/ul[1]/div[1]/a[1]/li[1]/span[1]").click()  # 打开平台角色
        time.sleep(3)

    def role_add(self):
        # 新增角色名称
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'新增')]")[0].click()  # 打开新增
        time.sleep(2)
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]").send_keys(
            "大管家")  # 添加角色名称
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//input[@placeholder='角色行政级别']").click()  # 选择行政级别
        time.sleep(2)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'社区/村')]")[1].click()  # 选择社区/村
        time.sleep(2)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'启用')]")[0].click()  # 状态选择启用
        time.sleep(2)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[0].click()  # 点击确认保存
        time.sleep(1)
        try:
            t = self.login.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]").text # 获取提交后的提示信息
            if t == '保存成功':
                print('角色名称新增成功')
        except:
            print('角色名称新增失败')
            return False
        else:
            return True

    def role_query(self):
        # 查询角色
        self.login.driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys(
        "大管家")  # 输入要查询内容
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'查询')]").click()  # 点击查询
        time.sleep(1)
        try:
            tt = self.login.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]").text # 获取提交后的提示信息
            if tt == '保存成功':
                print('角色名称查询成功')
        except:
            print('角色名称查询失败')
            return False
        else:
            return True

    def role_edit(self):
        #编辑角色
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-table__fixed-right')]//tr[1]//td[10]//div[1]//button[5]//span[1]").click()  # 打开编辑
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]").clear()  # 清除角色名称
        time.sleep(2)
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]").send_keys(
            "大管家1")  # 编辑角色名称
        time.sleep(2)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[0].click()  # 点击确认保存
        time.sleep(1)
        try:
            ttt = self.login.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]").text # 获取提交后的提示信息
            if ttt == '保存成功':
                print('角色名称编辑成功')
        except:
            print('角色名称编辑失败')
            return False
        else:
            return True

    def role_authorization(self):
        #授权角色
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-table__fixed-right')]//button[1]//span[1]").click()  # 打开菜单授权
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[5]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]").click()  # 选中门户配置
        time.sleep(2)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[2].click()  # 点击确认保存
        time.sleep(5)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-table__fixed-right')]//button[2]//span[1]").click()  # 打开大屏导航授权
        time.sleep(3)
        self.login.driver.find_element_by_xpath("//input[@placeholder='请输入导航名称']").send_keys("项目管理")  # 输入导航名称
        time.sleep(3)
        self.login.driver.find_element_by_xpath("//input[@placeholder='请选择分辨率']").click()  # 选择分辨率
        time.sleep(5)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'7680*2160')]")[81].click()  # 选择分辨率7680*2160
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'查询')]")[2].click()  # 点击查询
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[6]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]").click()  # 选中项目管理
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[3].click()  # 点击确认保存
        time.sleep(5)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-table__fixed-right')]//button[3]//span[1]").click()  # 打开app导航授权
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[4]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]").click()  # 选中预约单
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[1].click()  # 点击确认保存
        time.sleep(5)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'应用配置授权')]")[2].click()  # 打开应用配置授权
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[7]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]").click()  # 选中子系统
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[4].click()  # 点击确认保存
        time.sleep(1)
        try:
            tttt = self.login.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]").text  # 获取提交后的提示信息
            if tttt == '保存成功':
                print('菜单授权成功')
        except:
            print('菜单授权失败')
            return False
        else:
            return True

    def role_delete(self):
        #删除角色
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'应用配置授权')]")[2].click()  # 打开应用配置授权
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[7]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]").click()  # 选中子系统
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[4].click()  # 点击确认保存
        time.sleep(5)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-table__fixed-right')]//button[3]//span[1]").click()  # 打开app导航授权
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[4]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]").click()  # 选中预约单
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[1].click()  # 点击确认保存
        time.sleep(5)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-table__fixed-right')]//button[2]//span[1]").click()  # 打开大屏导航授权
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[6]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]").click()  # 选中项目管理
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[3].click()  # 点击确认保存
        time.sleep(5)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-table__fixed-right')]//button[1]//span[1]").click()  # 打开菜单授权
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[5]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]").click()  # 选中门户配置
        time.sleep(2)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确认')]")[2].click()  # 点击确认保存
        time.sleep(5)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-table__fixed-right')]//button[7]//span[1]").click()  # 删除角色名称
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[1].click()  # 点击确认保存
        time.sleep(1)
        try:
            ttttt = self.login.driver.find_element_by_xpath("//p[contains(text(),'删除成功')]").text # 获取提交后的提示信息
            if ttttt == '删除成功':
                print('角色名称删除成功')
        except:
            print('角色名称删除失败')
            return False
        else:
            return True
