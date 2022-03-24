import random
import time


class DepartmentManagement:
    '''
    部门管理--类型、职能、部门新增、查询、编辑、删除操作
    '''

    def __init__(self, login):
        self.login = login

    codes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    c = []
    while True:
        c.append(random.choice(codes))
        if len(c) == 5:
            break
    type_management_code = ''.join(c)  # 定义类型编号
    type_management_name = '自动化创建的类型名称{}'.format(random.choice(codes))  # 定义类型名称
    functional_name = '自动化创建的部门职能{}'.format(random.randint(1, 100))  # 定义职能名称
    department_name = '自动化创建的部门{}'.format(random.randint(20, 60))  # 定义部门名称

    def add_type_management(self):
        '''
        新增类型管理
        :return:
        '''
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'部门管理')]")[0].click()  # 点击‘部门管理’一级菜单
        time.sleep(1)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'类型管理')]")[0].click()  # 点击‘类型管理’二级菜单
        time.sleep(3)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'新增')]").click()  # 新增
        time.sleep(2)

        self.login.driver.find_element_by_xpath(
            "//div[@class='el-dialog']//div[1]//div[1]//div[1]//input[1]").send_keys(
            self.type_management_code)  # 部门类型编号输入框
        time.sleep(1)
        self.login.driver.find_element_by_xpath(
            "//div[@class='el-dialog__body']//div[2]//div[1]//div[1]//input[1]").send_keys(
            self.type_management_name)  # 部门类型名称输入框
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'确认')]").click()  # 确认
        time.sleep(1)
        try:
            self.login.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]")  # 获取提交后的提示信息
            print('类型管理新增成功，名称为：{}'.format(self.type_management_name))
        except:
            print('类型管理新增失败')
            return False
        else:
            return True

    def query_type_management(self):
        '''
        类型查询
        :return:
        '''
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//input[@placeholder='部门类型名称']").send_keys(
            self.type_management_name)  # 部门类型查询框
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'查询')]").click()  # 查询按钮
        time.sleep(3)
        try:
            name = self.login.driver.find_element_by_xpath(
                "//div[contains(@class,'el-table__body-wrapper is-scrolling-none')]//td[3]//div[1]").text  # 获取查询到类型名称
            if name == self.type_management_name:
                print('查询到新创建的类型，名称为：{}'.format(name))
                time.sleep(2)
                self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
                return True
            else:
                print('查询到的类型不是新创建的类型')
                time.sleep(2)
                self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
                return False
        except:
            print('未查询到类型数据')
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
            return False

    def edit_type_management(self):
        '''
        编辑类型管理
        :return:
        '''
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//input[@placeholder='部门类型名称']").send_keys(
            self.type_management_name)  # 获取查询到类型名称
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'查询')]").click()  # 查询
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'编辑')]")[-1].click()  # 编辑
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//textarea[contains(@class,'el-textarea__inner')]").send_keys(
            '编辑时填写的备注')  # 编辑备注字段
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'确认')]").click()  # 提交
        time.sleep(1)
        try:
            self.login.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]")  # 获取返回信息
            print('类型管理编辑成功，名称为：{}'.format(self.type_management_name))
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
        except:
            print('类型管理编辑失败')
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
            return False
        else:
            return True

    def delete_type_management(self):
        '''
        删除类型管理
        :return:
        '''
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//span[@class='el-icon-close']").click()  # 关闭菜单
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'类型管理')]").click()  # 点击类型管理二级菜单
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//input[@placeholder='部门类型名称']").send_keys(
            self.type_management_name)  # 输入类型查询
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'查询')]").click()  # 查询
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'删除')]")[-1].click()  # 删除
        time.sleep(1)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[1].click()  # 确定
        time.sleep(1)
        try:
            self.login.driver.find_element_by_xpath("//p[contains(text(),'删除成功')]")  # 获取提示信息
            print('类型管理删除成功，名称为：{}'.format(self.type_management_name))
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
        except:
            print('类型管理删除失败')
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
            return False
        else:
            return True

    def add_functional_management(self):
        '''
        新增职能管理
        :return:
        '''
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//span[@class='el-icon-close']").click()  # 关闭当前菜单
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'职能管理')]").click()  # 点击职能管理二级菜单
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'新增')]")[0].click()  # 新增
        time.sleep(1)

        self.login.driver.find_element_by_xpath(
            "//div[@class='el-input el-input--small']//input[@class='el-input__inner']").send_keys(
            self.functional_name)  # 输入部门职能名称
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'确认')]").click()  # 确认
        time.sleep(2)
        try:
            self.login.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]")  # 获取弹窗信息
            print('职能管理新增成功，名称为：{}'.format(self.functional_name))
        except:
            print('职能管理新增失败')
            return False
        else:
            return True

    def query_functional_management(self):
        '''
        职能查询
        :return:
        '''
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//input[@placeholder='部门职能名称']").send_keys(
            self.functional_name)  # 输入部门职能名称查询
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'查询')]").click()  # 查询
        time.sleep(3)
        try:
            name02 = self.login.driver.find_element_by_xpath(
                "//div[4]//div[2]//table[1]//tbody[1]//tr[1]//td[2]//div[1]").text  # 获取查询到的部门职能名称
            if name02 == self.functional_name:
                print('查询到新创建的职能，名称为：{}'.format(name02))
                time.sleep(2)
                self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
                return True
            else:
                print('查询到的职能不是新创建的职能')
                time.sleep(2)
                self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
                return False
        except:
            print('未查询到职能数据')
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
            return False

    def edit_functional_management(self):
        '''
        编辑职能
        :return:
        '''
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//input[@placeholder='部门职能名称']").send_keys(
            self.functional_name)  # 输入部门职能名称查询
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'查询')]").click()  # 查询
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-table__fixed-right')]//tr[1]//td[9]//div[1]//button[1]//span[1]").click()  # 编辑
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//textarea[contains(@class,'el-textarea__inner')]").send_keys(
            '编辑时填写的备注信息')  # 编辑备注信息
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'确认')]").click()  # 确认
        time.sleep(1)
        try:
            self.login.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]")  # 获取提示信息
            print('职能管理编辑成功，名称为：{}'.format(self.functional_name))
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
        except:
            print('职能管理编辑失败')
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
            return False
        else:
            return True

    def delete_functional_management(self):
        '''
        删除职能
        :return:
        '''

        time.sleep(2)
        self.login.driver.find_element_by_xpath("//span[@class='el-icon-close']").click()  # 关闭当前菜单
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'职能管理')]").click()  # 点击职能管理二级菜单
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//input[@placeholder='部门职能名称']").send_keys(
            self.functional_name)  # 输入部门职能名称查询
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'查询')]").click()  # 查询
        time.sleep(3)
        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-table__fixed-right')]//tr[1]//td[9]//div[1]//button[3]//span[1]").click()  # 删除
        time.sleep(2)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[1].click()  # 确认
        time.sleep(1)
        try:
            self.login.driver.find_element_by_xpath("//p[contains(text(),'删除成功')]")  # 获取弹窗信息
            print('职能管理删除成功，名称为：{}'.format(self.functional_name))
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
        except:
            print('职能管理删除失败')
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
            return False
        else:
            return True

    def add_department(self):
        '''
        新增部门
        :return:
        '''
        time.sleep(2)
        try:
            self.login.driver.find_element_by_xpath("//span[@class='el-icon-close']").click()  # 关闭当前菜单
        except:
            print('菜单未打开')
            self.login.driver.find_elements_by_xpath("//span[contains(text(),'部门管理')]")[0].click()  # 点击部门管理一级菜单
            time.sleep(1)
        time.sleep(2)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'部门管理')]")[1].click()  # 点击部门管理二级菜单
        time.sleep(3)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'新增')]").click()  # 新增
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//input[@placeholder='行政级别']").click()  # 点击行政级别
        time.sleep(1)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'街道/乡镇')]")[1].click()  # 选择行政级别
        time.sleep(1)

        self.login.driver.find_element_by_xpath(
            "//div[contains(@class,'el-form-item__content')]//input[contains(@placeholder,'部门名称')]").send_keys(
            self.department_name)  # 输入部门名称
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//input[@placeholder='部门全称']").click()  # 点击部门全称
        time.sleep(1)
        self.login.driver.find_element_by_xpath(
            "//div[@class='el-select el-select--small']//input[@placeholder='部门类型']").click()  # 点击部门类型
        time.sleep(1)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'职能 + 协调部门')]")[1].click()  # 选择部门类型
        time.sleep(1)
        self.login.driver.find_element_by_xpath(
            "//div[@class='el-select el-select--small']//input[@placeholder='部门职能']").send_keys(
            self.functional_name)  # 输入部门职能
        time.sleep(1)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'{}')]".format(self.functional_name))[
            1].click()  # 选择部门职能
        time.sleep(1)
        self.login.driver.find_element_by_xpath(
            "//div[@class='el-form-item__content']//i[@class='el-icon-caret-bottom']").click()  # 选择管辖区域
        time.sleep(1)
        self.login.driver.find_element_by_xpath(
            "//body[@class='el-popup-parent--hidden']/div[@id='app']/div[@class='app-wrapper openSidebar']/div[@class='main-container hasTagsView']/section[@class='app-main']/div[@class='app-container']/div[@class='head-container']/div[@class='el-dialog__wrapper']/div[@class='el-dialog']/div[@class='el-dialog__body']/div[@class='el-tree']/div[@class='el-tree-node is-focusable']/div[@class='el-tree-node__content']/span[1]").click()  # 展开区域
        time.sleep(1)
        self.login.driver.find_elements_by_class_name('el-checkbox')[1].click()  # 选择街道层级
        time.sleep(1)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[0].click()  # 确定
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'确认')]").click()  # 确认
        time.sleep(1)
        try:
            self.login.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]")  # 获取弹窗信息
            print('部门新增成功，名称为：{}'.format(self.department_name))
            time.sleep(2)
        except:
            print('部门新增失败')
            time.sleep(2)
            return False
        else:
            return True

    def query_department(self):
        '''
        部门查询
        :return:
        '''
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//input[@placeholder='部门名称或部门全称']").send_keys(
            self.department_name)  # 输入部门名称
        time.sleep(1)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'查询')]")[0].click()  # 查询
        time.sleep(3)
        try:
            name03 = self.login.driver.find_element_by_xpath(
                "//div[4]//div[2]//table[1]//tbody[1]//tr[1]//td[2]//div[1]").text  # 获取查询到的部门名称
            if name03 == self.department_name:
                print('查询到新创建的部门，名称为：{}'.format(name03))
                time.sleep(2)
                self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
                return True
            else:
                print('查询到的部门不是新创建的部门')
                time.sleep(2)
                self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
                return False
        except:
            print('未查询到部门数据')
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
            return False

    def edit_department(self):
        '''
        编辑部门
        :return:
        '''
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//input[@placeholder='部门名称或部门全称']").send_keys(
            self.department_name)  # 输入部门名称
        time.sleep(1)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'查询')]")[0].click()  # 查询
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'编辑')]")[-1].click()  # 编辑
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//textarea[contains(@class,'el-textarea__inner')]").send_keys(
            '编辑部门时填写的内容')  # 编辑备注
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//span[contains(text(),'确认')]").click()  # 确认
        time.sleep(1)
        try:
            self.login.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]")  # 获取弹窗信息
            print('部门编辑成功，名称为：{}'.format(self.department_name))
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
            time.sleep(2)
        except:
            print('部门编辑失败')
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
            time.sleep(2)
            return False
        else:
            return True

    def delete_department(self):
        '''
        删除部门
        :return:
        '''
        time.sleep(2)
        self.login.driver.find_element_by_xpath("//input[@placeholder='部门名称或部门全称']").send_keys(
            self.department_name)  # 输入部门名称
        time.sleep(1)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'查询')]")[0].click()  # 查询
        time.sleep(3)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'删除')]")[-1].click()  # 删除
        time.sleep(1)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[3].click()  # 确定
        time.sleep(1)
        try:
            self.login.driver.find_element_by_xpath("//p[contains(text(),'删除成功')]")  # 获取弹窗信息
            print('部门删除成功，名称为：{}'.format(self.department_name))
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
        except:
            print('部门删除失败')
            time.sleep(2)
            self.login.driver.find_element_by_xpath("//span[contains(text(),'重置')]").click()  # 重置
            return False
        else:
            return True
