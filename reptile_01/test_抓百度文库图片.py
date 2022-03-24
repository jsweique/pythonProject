import time

import requests
from selenium import webdriver


def down_pic(url, username, password):
    web = webdriver.Chrome()
    web.get(url)
    time.sleep(3)
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
    web.execute_script('window.scrollTo(0,3800)')  # 向下滑动页面
    time.sleep(2)

    imgs = web.find_elements_by_tag_name('img')
    n = 1
    for img in imgs:
        i = img.get_attribute('src')
        try:
            resp = requests.get(i)
            with open(r'C:\Users\zheng\PycharmProjects\pythonProject\reptile_01\img\{}.jpg'.format(n), mode='wb') as w:
                w.write(resp.content)
            print("下载成功，链接：" + i)
            n += 1
        except:
            print('下载失败，链接：' + str(i))
        print(i)
    web.quit()


url = r'https://wenku.baidu.com/view/82de636483c758f5f61fb7360b4c2e3f572725c8.html?fixfr=Bw0MJgEj1fIyCC%252FDSi88Ew%253D%253D&fr=income1-wk_go_search-search'
down_pic(url, '15152151131', 'zhengxinyang')
