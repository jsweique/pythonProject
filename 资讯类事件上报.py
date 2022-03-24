# encoding:utf-8
#嵌套式定位
from PIL import Image
import pytesseract
import time
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pywinauto.keyboard import send_keys
import pywinauto
#  pip install pywinauto
import random
nubA =  random.randint(1,10000)
nubB = str(nubA)

''''''
dt = datetime.now()
print(f'今天是：{dt.year}年{dt.month}月{dt.day}日 {dt.hour}:{dt.minute}:{dt.second}')

def tes(list):
    list1 = []

    for i in list:
        if i.isdigit():
            list1.append(i)
    return ''.join(list1)

url = 'http://192.168.20.214:10001/'
driver = webdriver.Chrome()
driver.maximize_window()  # 将浏览器最大化
driver.get(url)


# 截取当前网页并放到D盘下命名为printscreen，该网页有我们需要的验证码
driver.save_screenshot(r"C:\yanzhengma\photo0001.png")
imgelement = driver.find_element_by_id('imgCode')  # 定位验证码
location = imgelement.location  # 获取验证码x,y轴坐标
#print(location)
size = imgelement.size  # 获取验证码的长宽
#print(size)
rangle = (int(location['x'] + 310), int(location['y'] + 130), int(location['x'] + size['width'] + 320),
          int(location['y'] + size['height'] + 135))  # 写成我们需要截取的位置坐标
i = Image.open(r"C:\yanzhengma\photo0001.png")  # 打开截图
frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
frame4 = frame4.convert('RGB')
frame4.save(r"C:\yanzhengma\photo0002.png")  # 保存我们接下来的验证码图片 进行打码

time.sleep(1)

pytesseract.pytesseract.tesseract_cmd = 'C:/Tesseract-OCR/tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:/Tesseract-OCR/tessdata"'
image = Image.open(r"C:\yanzhengma\photo0002.png")

list2 = list(pytesseract.image_to_string(image))
t = tes(list2)

# code =pytesseract.image_to_string(image)
#code = pytesseract.image_to_string(image, config=tessdata_dir_config)
#print(code)
time.sleep(1)
driver.find_element_by_id('loginname').send_keys('10000')
time.sleep(1)
driver.find_element_by_id('password').send_keys('pxzz258369')
time.sleep(1)

driver.find_element_by_id('ValidateCode').send_keys(t)     #验证码已录入，需要先获保存证码本地文件

time.sleep(1)
driver.find_element_by_xpath("//input[@id='btnSubmit']").click()
time.sleep(2)

driver.get("http://192.168.20.214:10001/adminHome/index")
time.sleep(2)
driver.find_element_by_link_text("事件订单库").click()
time.sleep(1)
driver.find_element_by_xpath("//div[@class='menu-box']/ul[@id='grandpa']/li/ul[@class='list-unstyled hd mcc']/li[3]/ul[1]/li[5]/a[1]/span[2]").click()
time.sleep(1)
driver.switch_to.frame(1)  #切换iframe
time.sleep(1)
driver.find_element_by_id('btn_create').click()   #点击新增
time.sleep(2)
Select(driver.find_element_by_xpath("//select[@id='EnumEventProcType']")).select_by_visible_text("预警推送")
driver.find_element_by_xpath("//input[@id='name']").send_keys("咨询"+ nubB)

driver.find_element_by_xpath("//textarea[@id='memo']").send_keys("事情是这样的 ，·····2" +  nubB)

driver.find_element_by_xpath("//textarea[@id='addr']").send_keys("地址是在这里2" + nubB)

driver.find_element_by_xpath("//div[7]//div[1]//div[1]//a[1]//i[1]").click()  # 点击上传图片
time.sleep(2)
"""上传图片"""
#from pywinauto.keyboard import send_keys
#import pywinauto
#  pip install pywinauto

# 使用pywinautoc创建一个操作桌面窗口的对象
win1= pywinauto.Desktop()
# 选择文件上传的窗口 窗口句柄默认为‘打开’
time.sleep(1)
bow1 = win1['打开']
time.sleep(1)
# 选择文件地址输入框，点击激活
bow1["Toolbar3"].click()
time.sleep(1)
# 键盘输入上传文件的路径
send_keys(r"E:/")
time.sleep(1)
 # 键盘输入回车，打开该路径
send_keys("{VK_RETURN}")
time.sleep(1)
# 选中文件名输入框，输入文件名
bow1["文件名(&N):Edit"].type_keys("photo0002.png")
time.sleep(1)
# bow1["文件名(&N):Edit"].click()
# send_keys("xx文件名")
# 点击打开
bow1["打开(&O)"].click()

time.sleep(2)
"""上传图片"""

driver.find_element_by_xpath("//a[@id='btn_setMap']").click()  #事件GIS定位
time.sleep(1)
Select(driver.find_element_by_xpath("//select[@id='department_2']")).select_by_visible_text("徐州市沛县/敬安镇/")
time.sleep(1)
Select(driver.find_element_by_xpath("//select[@id='department_1']")).select_by_value("0e0da265-b65d-4043-a428-d62092c51a7b")
time.sleep(1)
Select(driver.find_element_by_xpath("//select[@id='department_0']")).select_by_index(1)
time.sleep(1)

driver.find_element_by_xpath("//button[@id='btn_showArea']").click() #点击选定网格
time.sleep(2)
driver.find_element_by_xpath("//*[name()='path' and contains(@stroke-linejoin,'round')]").click()   #选定网格
time.sleep(1)
driver.find_element_by_xpath("//button[contains(@class,'btn btn-success btn-block btn_sub')]").click()  #点击提交
time.sleep(1)
driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()  #确认
time.sleep(1)
driver.find_element_by_xpath('//*[@id="layui-layer100008"]/div[3]/a').click() # 确认
time.sleep(2)
tex = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
print(tex)

time.sleep(2)

driver.close()
"""审批"""
time.sleep(3)

def tes(list):
    list1 = []
    for i in list:
        if i.isdigit():
            list1.append(i)
    return ''.join(list1)

url = 'http://192.168.20.214:10001/'
driver = webdriver.Chrome()
driver.maximize_window()  # 将浏览器最大化
driver.get(url)


# 截取当前网页并放到D盘下命名为printscreen，该网页有我们需要的验证码
driver.save_screenshot(r"E:\photo0003.png")
imgelement = driver.find_element_by_id('imgCode')  # 定位验证码
location = imgelement.location  # 获取验证码x,y轴坐标
#print(location)
size = imgelement.size  # 获取验证码的长宽
#print(size)
rangle = (int(location['x'] + 310), int(location['y'] + 130), int(location['x'] + size['width'] + 320),
          int(location['y'] + size['height'] + 135))  # 写成我们需要截取的位置坐标
i = Image.open(r"E:\photo0003.png")  # 打开截图
frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
frame4 = frame4.convert('RGB')
frame4.save(r"E:\photo0004.png")  # 保存我们接下来的验证码图片 进行打码

time.sleep(1)

pytesseract.pytesseract.tesseract_cmd = 'E:/Tesseract-OCR/tesseract.exe'
tessdata_dir_config = '--tessdata-dir "E:/Tesseract-OCR/tessdata"'
image = Image.open(r"E:\photo0004.png")

list2 = list(pytesseract.image_to_string(image))
t = tes(list2)

# code =pytesseract.image_to_string(image)
#code = pytesseract.image_to_string(image, config=tessdata_dir_config)
#print(code)
time.sleep(1)
driver.find_element_by_id('loginname').send_keys('JAZRS')
time.sleep(1)
driver.find_element_by_id('password').send_keys('123456')
time.sleep(1)

driver.find_element_by_id('ValidateCode').send_keys(t)     #验证码已录入，需要先获保存证码本地文件

time.sleep(1)
driver.find_element_by_xpath("//input[@id='btnSubmit']").click()
time.sleep(2)

driver.get("http://192.168.20.214:10001/adminHome/index")
time.sleep(3)
driver.find_element_by_xpath("//ul[@id='grandpa']/li/ul[@class='list-unstyled hd mcc']/li[9]/a[1]/span[2]").click()
time.sleep(1)
driver.find_element_by_xpath("//ul[@id='grandpa']/li/ul[@class='list-unstyled hd mcc']/li[9]/ul[1]/li[1]/a[1]/span[2]").click()
time.sleep(1)
driver.switch_to.frame(1)  #切换iframe
time.sleep(1)
driver.find_element_by_xpath("//input[@id='EventRecordCode']").send_keys(tex)
driver.find_element_by_xpath("//tr[1]//td[3]//a[1]//span[1]").click()
time.sleep(3)
driver.switch_to.parent_frame() #切换回父级iframe
time.sleep(2)
driver.switch_to.frame(2)  #切换至2 iframe
time.sleep(2)
driver.find_element_by_xpath("//button[@id='btn_show_proceed']").click()
time.sleep(1)
driver.find_element_by_xpath("//textarea[@id='Result']").send_keys("处理成功，这次就这样吧")
time.sleep(1)
driver.find_element_by_xpath("//span[@class='glyphicon glyphicon-plus-sign']").click()
"""上传图片"""
# 使用pywinautoc创建一个操作桌面窗口的对象
win1= pywinauto.Desktop()
# 选择文件上传的窗口 窗口句柄默认为‘打开’
time.sleep(1)
bow1 = win1['打开']
time.sleep(1)
# 选择文件地址输入框，点击激活
bow1["Toolbar3"].click()
time.sleep(1)
# 键盘输入上传文件的路径
send_keys(r"E:/")
time.sleep(1)
 # 键盘输入回车，打开该路径
send_keys("{VK_RETURN}")
time.sleep(1)
# 选中文件名输入框，输入文件名
bow1["文件名(&N):Edit"].type_keys("photo0004.png")
time.sleep(1)
# bow1["文件名(&N):Edit"].click()
# send_keys("xx文件名")
# 点击打开
bow1["打开(&O)"].click()
time.sleep(2)
"""上传图片"""
driver.find_element_by_xpath("//button[@id='btn_proceed']").click()
time.sleep(1)
driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()

time.sleep(2)
driver.close()
time.sleep(2)

"""评价"""

def tes(list):
    list1 = []

    for i in list:
        if i.isdigit():
            list1.append(i)
    return ''.join(list1)

url = 'http://192.168.20.214:10001/'
driver = webdriver.Chrome()
driver.maximize_window()  # 将浏览器最大化
driver.get(url)


# 截取当前网页并放到D盘下命名为printscreen，该网页有我们需要的验证码
driver.save_screenshot(r"E:\photo0001.png")
imgelement = driver.find_element_by_id('imgCode')  # 定位验证码
location = imgelement.location  # 获取验证码x,y轴坐标
#print(location)
size = imgelement.size  # 获取验证码的长宽
#print(size)
rangle = (int(location['x'] + 310), int(location['y'] + 130), int(location['x'] + size['width'] + 320),
          int(location['y'] + size['height'] + 135))  # 写成我们需要截取的位置坐标
i = Image.open(r"E:\photo0001.png")  # 打开截图
frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
frame4 = frame4.convert('RGB')
frame4.save(r"E:\photo0002.png")  # 保存我们接下来的验证码图片 进行打码

time.sleep(1)

pytesseract.pytesseract.tesseract_cmd = 'E:/Tesseract-OCR/tesseract.exe'
tessdata_dir_config = '--tessdata-dir "E:/Tesseract-OCR/tessdata"'
image = Image.open(r"E:\photo0002.png")

list2 = list(pytesseract.image_to_string(image))
t = tes(list2)

# code =pytesseract.image_to_string(image)
#code = pytesseract.image_to_string(image, config=tessdata_dir_config)
#print(code)
time.sleep(1)
driver.find_element_by_id('loginname').send_keys('10000')
time.sleep(1)
driver.find_element_by_id('password').send_keys('pxzz258369')
time.sleep(1)

driver.find_element_by_id('ValidateCode').send_keys(t)     #验证码已录入，需要先获保存证码本地文件

time.sleep(1)
driver.find_element_by_xpath("//input[@id='btnSubmit']").click()
time.sleep(2)

driver.get("http://192.168.20.214:10001/adminHome/index")
time.sleep(2)
driver.find_element_by_link_text("事件订单库").click()
time.sleep(1)
driver.find_element_by_xpath("//div[@class='menu-box']/ul[@id='grandpa']/li/ul[@class='list-unstyled hd mcc']/li[3]/ul[1]/li[5]/a[1]/span[2]").click()
time.sleep(1)
driver.switch_to.frame(1)  #切换iframe
time.sleep(1)
driver.find_element_by_xpath("//tr[1]//td[3]//a[1]//span[1]").click()
time.sleep(2)
driver.switch_to.parent_frame() #切换回父级iframe
time.sleep(2)
driver.switch_to.frame(2)  #切换至2 iframe
time.sleep(2)
driver.find_element_by_xpath("//textarea[@id='Evaluation']").clear()
time.sleep(1)
#data = dt.year + dt.month + dt.day
driver.find_element_by_xpath("//textarea[@id='Evaluation']").send_keys("处理的非常好！！"+ nubB)
time.sleep(1)
driver.find_element_by_xpath("//button[@id='btn_sub']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
time.sleep(3)
"""归档"""
driver.switch_to.parent_frame() #切换回父级iframe
time.sleep(2)
driver.switch_to.frame(1)  #切换至1 iframe
time.sleep(2)

driver.find_element_by_xpath("//tr[1]//td[3]//a[1]//span[1]").click()
time.sleep(2)
driver.switch_to.parent_frame() #切换回父级iframe
time.sleep(2)
driver.switch_to.frame(2)  #切换至2 iframe
time.sleep(2)
driver.find_element_by_xpath("//button[@id='btn_sub']").click()
time.sleep(1)
driver.find_element_by_xpath("//a[@class='layui-layer-btn0']").click()
time.sleep(4)
driver.close()
dt = datetime.now()
print(f'现在是：{dt.year}年{dt.month}月{dt.day}日 {dt.hour}:{dt.minute}:{dt.second}')