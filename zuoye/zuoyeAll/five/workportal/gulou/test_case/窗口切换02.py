import random
import time

import ddddocr
from PIL import Image
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()


def log_bussinessCenter():
    driver.get('http://192.168.20.243:9083/login?redirect=%2Fconsole')

    driver.find_element_by_xpath(
        '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/input[1]').send_keys(
        'jswq168')
    time.sleep(1)
    driver.find_element_by_xpath('//form[1]/div[3]/div[1]/div[1]/div[2]/input[1]').send_keys('xsw2CDE#168')
    time.sleep(1)

    driver.save_screenshot(r"c:\yanzhengma\photo0001.png")
    code = driver.find_element_by_xpath("//*[@class='login-code']")
    location = code.location
    size = code.size
    rangle = (int(location['x'] + 340), int(location['y'] + 146),
             int(location['x'] + size['width'] + 380),
             int(location['y'] + size['height'] + 152))

    i = Image.open(r"C:\yanzhengma\photo0001.png").crop(rangle)
    i.save(r"C:\yanzhengma\photo0002.png")

    ocr = ddddocr.DdddOcr()
    with open(r"C:\yanzhengma\photo0002.png", 'rb') as f:
        img_bytes = f.read()
    t = ocr.classification(img_bytes)

    driver.find_elements_by_class_name('el-input__inner')[2].send_keys(t)
    time.sleep(1)

    driver.find_element_by_css_selector("button").click()
    time.sleep(2)

def window_switch():
    mask=[]
    for i in range(3,6):
        driver.find_element_by_xpath("//div[@class='el-carousel__item is-active is-animating']//div[{}]".format(i)).click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        mask.append(driver.title)
        #print(driver.title)
        driver.switch_to.window(driver.window_handles[0])
    print(mask)
    # for i in driver.window_handles:
    #     driver.switch_to.window(i)
    #     if driver.title == '项目全生命周期':
    #         driver.close()
    #         print('成功关闭该窗口')
    #         driver.switch_to.window(driver.window_handles[0])
    #         print(driver.title)
    #         break
    #     else:
    #         continue

    current_window=driver.current_window_handle
    print('curr'+driver.title)
    for ii in driver.window_handles:
        print(driver.title)
        # if ii != current_window:
        #     driver.switch_to.window(ii)
        #     if driver.title == '徐州市鼓楼区审批服务综合执法一体化平0000022台':
        #         time.sleep(1)
                # driver.close()

def iframe_switch():
    driver.find_element_by_xpath("//div[contains(@class,'Myuse el-col el-col-6 el-col-offset-2')]//div[contains(@class,'cp')]").click()
    time.sleep(2)
    driver.find_elements_by_xpath("//h4[contains(text(),'网格化')]")[0].click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element_by_xpath("//p[contains(text(),'后台数据管理')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[contains(text(),'事件订单库')]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//span[contains(text(),'市场管理')]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//span[contains(text(),'非法虚假')]").click()
    time.sleep(2)
    #切换iframe
    driver.switch_to.frame(driver.find_element_by_xpath("//div[@class='tabs-panels']//div[2]//div[1]//iframe[1]"))

    driver.find_element_by_id('btn_create').click()


def add_shopCalendar():
    time.sleep(1)
    driver.find_element_by_xpath(
        "//body/div[@id='app']/div[contains(@class,'pages')]/div[contains(@class,'UserCenter')]/div[contains(@class,'mt20 el-row is-justify-space-around el-row--flex')]/div[contains(@class,'workDay el-col el-col-8')]/div[contains(@class,'myCalendar fc fc-media-screen fc-direction-ltr fc-theme-standard')]/div[contains(@class,'fc-view-harness fc-view-harness-active')]/div[contains(@class,'fc-daygrid fc-dayGridMonth-view fc-view')]/table[contains(@class,'fc-scrollgrid-liquid')]/tbody/tr[contains(@class,'fc-scrollgrid-section-liquid')]/td/div[contains(@class,'fc-scroller-harness fc-scroller-harness-liquid')]/div[contains(@class,'fc-scroller fc-scroller-liquid-absolute')]/div[contains(@class,'fc-daygrid-body fc-daygrid-body-unbalanced')]/table[contains(@class,'fc-scrollgrid-sync-table')]/tbody/tr[1]/td[2]/div[1]/div[1]").click()
    time.sleep(2)
    # CSS元素定位
    driver.find_elements_by_css_selector('span.el-radio-button__inner')[1].click()
    time.sleep(1)
    name = '这是填写的事件标题{}'.format(random.randint(1, 20))
    # class_name元素定位
    driver.find_elements_by_class_name('el-input__inner')[2].send_keys(name)
    time.sleep(2)
    # xpath相对路径
    driver.find_element_by_xpath("//textarea[@placeholder='请输入事件描述']").send_keys('事件描述')
    time.sleep(2)
    driver.find_element_by_xpath("//div[contains(@class,'el-dialog__wrapper')]//div[3]//div[1]//button[1]").click()
    time.sleep(2)
    # xpath绝对路径
    t = driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[2]/div[1]/a[1]/div[3]").text
    print('获取到的工作日历名称是：{}'.format(t))
    time.sleep(2)
def edit_shopCalendar():
    driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[2]/div[1]/a[1]/div[3]").click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//textarea[@placeholder='请输入事件描述']").clear()
    except:
        print('未找到元素')
        return False
    else:
        print('找到元素')
        pass
    time.sleep(1)
    driver.find_element_by_xpath("//textarea[@placeholder='请输入事件描述']").send_keys('编辑时填写的内容')
    time.sleep(1)
    driver.find_element_by_xpath("//div[contains(@class,'el-dialog__wrapper')]//div[3]//div[1]//button[1]").click()
    time.sleep(2)
    try:
        tt = driver.find_element_by_xpath('//p[contains(text(),"修改成功")]').text
        time.sleep(1)
        if tt == '修改成功':
            print('工作日历编辑成功')
            return True
        else:
            print('编辑失败！！')
            return False
    except:
        print('未获取编辑的提示')
        return False

#if\while语句案例
while True:
    log_bussinessCenter()
    title = driver.title
    if title == '个人工作台 - 智慧鼓楼工作门户':
        break
    else:
        continue

#异常案例
# add_shopCalendar()
# edit_shopCalendar()

#切换窗口案例
window_switch()

#切换iframe
# iframe_switch()

# driver.quit()
time.sleep(3)
driver.close()
