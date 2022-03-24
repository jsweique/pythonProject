import time

class shouye:
    def __init__(self, login):
        self.login = login

    def add_shouye(self, num):
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//div[@class='note el-col el-col-6']//div[@class='cp']").click() #找到便签位置
        time.sleep(1)
        self.login.driver.find_element_by_css_selector("div.pages div.UserCenter:nth-child(2) div.mt20.el-row.is-justify-space-around.el-row--flex:nth-child(2) div.note.el-col.el-col-6 div.myTItle div.myTItle-top > div.myTItle-top-subjoin.cp").click() #打开便签
        time.sleep(1)
        self.login.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[6]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/textarea[1]").send_keys(num) #添加便签内容
        time.sleep(1)
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'保存')]")[0].click() #对添加的便签内容进行保存
        time.sleep(1)
        a = self.login.driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]").text  # 获取元素文本内容
        print("认真" + a)  # 打印
        time.sleep(1)

    def edit_shouye(self, nu):
        self.login.driver.find_elements_by_xpath("//div[contains(text(),'{}')]".format(nu))[0].click()  # 打开便签
        time.sleep(1)
        self.login.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[6]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/textarea[1]").clear()  # 清除已有便签内容
        time.sleep(1)
        self.login.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[6]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/textarea[1]").send_keys("好好学习")  # 重新输入便签内容
        self.login.driver.find_elements_by_xpath("//span[contains(text(),'保存')]")[0].click()  # 保存更新的编辑内容
        time.sleep(1)
        try:
            tt = self.login.driver.find_element_by_xpath('//p[contains(text(),"修改成功")]').text
            if tt == '修改成功':
                print('便签编辑成功')
            else:
                print('编辑失败！！')
        except:
            print('未获取编辑的提示')
        time.sleep(1)

    def delete_shouye(self, nu):
        self.login.driver.find_elements_by_xpath("//div[contains(text(),'{}')]".format(nu))[0].click() #打开添加的便签内容
        time.sleep(1)
        self.login.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[6]/div[1]/div[3]/div[1]/button[2]/span[1]").click() #点击删除便签
        time.sleep(1)
        self.login.driver.find_element_by_xpath("//button[contains(@class,'el-button el-button--default el-button--small el-button--primary')]//span").click() #点击确定删除
        time.sleep(1)
        try:
            ttt = self.login.driver.find_element_by_xpath('//p[contains(text(),"删除成功")]').text
            if ttt == '删除成功':
                print('便签删除成功')
            else:
                print('删除失败！！')
        except:
                print('未获取到删除的提示')
        time.sleep(1)

