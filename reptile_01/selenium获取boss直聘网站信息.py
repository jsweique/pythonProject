import time

from selenium import webdriver

web = webdriver.Chrome()
web.get(r'https://www.zhipin.com/?ka=header-home')
web.maximize_window()
time.sleep(1)
web.find_element_by_xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/div[2]/p/input').send_keys('测试工程师')
time.sleep(1)
web.find_element_by_xpath('//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/button').click()
time.sleep(3)

div_list = web.find_elements_by_xpath('//div[@class="primary-box"]/div[1]/span[2]')


def down_message():
    n = 1
    for i in div_list:
        try:
            i.click()
            time.sleep(1)
            web.switch_to.window(web.window_handles[-1])  # 切换浏览器窗口到最后一个
            text = web.find_elements_by_xpath('//div[@class="job-sec"]')[0].text
            gongshang = web.find_elements_by_xpath('//div[@class="job-sec"]')[1].text
            address = web.find_elements_by_xpath('//div[@class="job-sec"]')[2].text
            with open(r'C:\Users\zheng\PycharmProjects\pythonProject\reptile_01\img\{}.txt'.format(n), mode='w',
                      encoding='utf-8') as w:
                w.write(text + '\r\n')
                w.write(gongshang + '\r\n')
                w.write(address)
            web.close()
            web.switch_to.window(web.window_handles[0])
            time.sleep(1)
            n += 1
            break
        except:
            print('打开失败，n是：{}'.format(n))
            time.sleep(2)
        print('该页数据下载完毕，n是：'.format(n))


down_message()
time.sleep(2)

while 1:
    w = web.find_elements_by_xpath('//div[@class="job-list"]/div[3]/a')[-1]  # 获取分页
    print(w.get_attribute('href'))
    if w.get_attribute('href') != 'javascript:;':
        w.click()  # 报错了
        down_message()
    else:
        break

web.quit()
