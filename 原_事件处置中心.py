import time

from selenium import webdriver


class OldEventHandle:
    def __init__(self,login,code):
        self.login=login
        self.code=code

    def old_event_handle(self):
        pass



d=webdriver.Chrome()
d.find_element_by_link_text('后台数据管理控制台').click()
time.sleep(1)
d.find_element_by_xpath("//div[@class='swiper-slide swiper-slide-active']//div[@class='swiper-slide--content']//a").click()
time.sleep(3)
d.find_elements_by_link_text('事件处置中心')[0].click()
time.sleep(3)
d.find_element_by_id('keyword').send_keys(code)
time.sleep(1)
d.find_element_by_id('query_btn').click()
time.sleep(1)
d.find_element_by_xpath("//div[@class='table-tr']//span[contains(text(),'0926')]").click()
time.sleep(2)
d.find_element_by_id('show_event_detail').click()
time.sleep(2)
d.find_element_by_id('btn_cz').click()
time.sleep(1)
