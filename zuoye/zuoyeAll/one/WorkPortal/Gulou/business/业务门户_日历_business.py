import time
import datetime

class Calendar:
    #登录
    def __init__(self, login):
        self.login = login

    #新增两条日历
    def add_Calendar(self):
        self.login.driver.implicitly_wait(5)

        for i in range(2):
            # 获取系统当前日期，选择日历
            now = datetime.datetime.now()
            day = str(now.strftime("%d") + "日")
            self.login.driver.find_element_by_xpath("//a[contains(text(),'" + day + "')]").click()
            time.sleep(2)

            #根据系统时间设置变量
            T = str(now.strftime("%H:%M:%S"))

            add_title = str(T + "新增测试日历")
            self.login.driver.find_elements_by_class_name("el-input__inner")[2].send_keys(add_title)
            time.sleep(2)

            self.login.driver.find_element_by_tag_name("textarea").send_keys(add_title)
            time.sleep(2)

            self.login.driver.find_element_by_xpath("//span[contains(text(),'确认')]").click()
            time.sleep(2)

            add_title = self.login.driver.find_element_by_xpath("//div[contains(text(),'" + add_title + "')]" ).text
            print(add_title + "成功")
            print("----------------------------------------------")

            if i==0:
                global ADD1
                ADD1 = T
                continue

            else:
                global ADD2
                ADD2 = T
                break


    #修改新增的第一条日历
    def edit_Calendar(self):
        self.login.driver.implicitly_wait(5)

        global ADD1
        self.login.driver.find_element_by_xpath("//div[contains(text(),'" + ADD1 + "')]").click()
        time.sleep(2)

        self.login.driver.find_element_by_css_selector("input[placeholder='选择日期时间']").click()
        time.sleep(2)

        self.login.driver.find_element_by_xpath("//span[contains(text(),'此刻')]").click()
        time.sleep(2)

        self.login.driver.find_element_by_xpath("//span[contains(text(),'重要')]").click()
        time.sleep(2)

        self.login.driver.find_elements_by_class_name("el-input__inner")[2].clear()
        time.sleep(1)

        edit_title = str("修改"+ADD1 + "的日历")
        self.login.driver.find_elements_by_class_name("el-input__inner")[2].send_keys(edit_title)
        time.sleep(2)

        self.login.driver.find_element_by_tag_name("textarea").send_keys("+修改时间为此刻+程度为重要")
        time.sleep(2)

        self.login.driver.find_element_by_xpath("//span[contains(text(),'确认')]").click()
        time.sleep(2)

        edit_title = self.login.driver.find_element_by_xpath("//div[contains(text(),'" + ADD1 + "')]").text
        print(edit_title + "成功")
        print("----------------------------------------------")


    #删除新增日历
    def delete_Calendar(self):

        self.login.driver.implicitly_wait(5)

        global ADD2
        self.login.driver.find_element_by_xpath("//div[contains(text(),'" + ADD2 + "')]").click()
        time.sleep(2)

        self.login.driver.find_elements_by_xpath("//span[contains(text(),'删除')]")[1].click()
        time.sleep(2)

        self.login.driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[1].click()
        time.sleep(2)

        print("删除"+ADD2+"的日历成功")
        print("----------------------------------------------")
        time.sleep(3)
        self.login.driver.find_element_by_xpath("//li[contains(text(),'工作日历')]").click()
        time.sleep(3)

        global ADD1
        self.login.driver.find_element_by_xpath("//div[contains(text(),'" + ADD1 + "')]").click()
        time.sleep(2)

        self.login.driver.find_element_by_xpath("//span[contains(text(),'删除')]").click()
        time.sleep(2)

        self.login.driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
        time.sleep(2)

        print("删除"+ADD1+"的日历成功")
        print("----------------------------------------------")
        time.sleep(1)


