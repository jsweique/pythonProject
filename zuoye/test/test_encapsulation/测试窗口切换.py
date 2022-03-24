import time

from zuoye.test.config.browser import Browser
from zuoye.test.config.业务中心登录_business import Login
from zuoye.test.config.窗口切换 import WindowSwitch
from zuoye.test.test_encapsulation.键盘事件 import mouse_hover, calendar_send, scroll_get_element, scroll_element
from zuoye.test.全局变量 import OverallSituationTest

# o=OverallSituationTest(r'http://192.168.20.243:9083/console','jswq168','xsw2CDE#168')
# o.overall_situation_test()
# o.test_login()
#
# def test_switch_windows():
#     mask = []
#     masks=['用户中心','物联中台','区域管理','指挥调度','城市门户']
#     o.driver.find_element_by_xpath("//li[contains(text(),'应用中心')]").click()
#     time.sleep(2)
#     for i in masks:
#         o.driver.find_element_by_xpath("//h4[contains(text(),'{}')]".format(i)).click()
#         time.sleep(1)
#         o.driver.switch_to.window(o.driver.window_handles[-1])
#         mask.append(o.driver.title)
#         # print(driver.title)
#         o.driver.switch_to.window(o.driver.window_handles[0])
#     print(mask)
# test_switch_windows()


# from zuoye.workportal.gulou.business.登录_business import Login
# from zuoye.workportal.gulou.config.browser import Browser
# from zuoye.workportal.gulou.config.文件上传 import UploadFile
# from zuoye.workportal.gulou.config.窗口切换 import WindowSwitch

br = Browser(r'http://192.168.20.243:9083')
br.browser()
# Login(br).login('jswq168', 'xsw2CDE#168')
# win = WindowSwitch(br)
# win.swtich_last('指挥调度')
# for i in range(10):
#     time.sleep(1)
#     print(i)

# br.driver.find_element_by_xpath("//img[@class='avatar']").click()
# time.sleep(1)
# f1=br.driver.find_element_by_xpath("//i[@class='vicp-icon1']")
# f1.click()

# u=UploadFile()
# path=r'C:\Users\zheng\Desktop\图片\1126375876_15976285148491n.jpg'
# # u.upload_file_py(r'C:\Users\zheng\Desktop\图片\1126375876_15976285148491n.jpg')
# u.upload_file(path)

# iframe=br.driver.find_element_by_xpath("//div[@class='tabs-panels']//div[2]//div[1]//iframe[1]")
# br.driver.switch_to.frame(iframe)
# time.sleep(2)

# calendar_send(br,'class', 'el-input__inner', '2002-12-12 20:12',12)
#
# br.driver.find_element_by_class_name()

# br.driver.get('http://www.imooc.com/read')
# time.sleep(3)
# # path="//li[@class='clearfix']"
# # scroll_get_element(br,path,'title','进阶量化交易')
#
#
# scroll_element(br,'xpath',"//p[contains(text(),'--Java')]")
