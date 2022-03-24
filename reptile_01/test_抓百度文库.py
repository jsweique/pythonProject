import time

import requests
from lxml import etree
from selenium import webdriver


# requests抓取第一页的内容
class FuncFirst:
    def __init__(self):
        pass
    def func_first(self,url):
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        et = etree.HTML(resp.text)
        etr = et.xpath("//div[@id='reader-container']/div//div[@class='reader-txt-layer']/div/p/text()")
        print(''.join(etr).strip())


# selenium抓取第二页之后的内容
class FuncAll:
    def __init__(self):
        pass

    def func_get_message(self, web):
        web.execute_script('window.scrollTo(0,3800)')  # 向下滑动页面
        time.sleep(2)
        try:
            web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/span').click()
            print('点击继续阅读成功')
            time.sleep(2)
            web.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # 滑动到底部，否则只能抓取前5/6页的内容
            time.sleep(10)
        except:
            print('点击继续阅读失败！！！')
        we = web.find_elements_by_class_name('ie-fix')
        for ee in we:
            print(ee.text.strip())

    # 登录，获取全部内容
    def func_all_login(self, url, username, password):
        web = webdriver.Chrome()
        web.get(url)
        web.maximize_window()
        time.sleep(2)
        web.find_element_by_xpath("//div[@class='user-icon']").click()
        time.sleep(3)
        try:
            web.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        except:
            pass
        time.sleep(1)
        web.find_element_by_xpath("//input[@id='TANGRAM__PSP_11__userName']").send_keys(username)
        web.find_element_by_xpath("//input[@id='TANGRAM__PSP_11__password']").send_keys(password)
        web.find_element_by_id('TANGRAM__PSP_11__submit').click()
        time.sleep(5)
        web.refresh()
        time.sleep(2)
        self.func_get_message(web)

    # 抓取前3页内容，不登录，点击继续阅读
    def func_all(self, url):
        web = webdriver.Chrome()
        web.get(url)
        self.func_get_message(web)


url = r'https://wenku.baidu.com/view/a414cdad69ec0975f46527d3240c844769eaa0de.html?fixfr=4TD%252B5QbGXIt8XOUzrwXyDQ%253D%253D&fr=income9-wk_go_searchX-search'

FuncFirst().func_first(url)
# FuncAll().func_all(url)
# FuncAll().func_all_login(url, '15152151131', 'zhengxinyang')
