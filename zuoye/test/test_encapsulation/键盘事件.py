import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def mouse_hover(br, element):
    '''
    鼠标悬浮
    br是传入的浏览器对象，需要加上.driver传入ActionChains
    '''
    act = ActionChains(br.driver)
    act.move_to_element(element).perform()


# def refresh_f5(br):
#     '''
#     强制刷新
#     '''
#     act = ActionChains(br.driver)
#     act.key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()


def js_excute_calendar(driver, by, value, index=None):
    '''
    执行js，去除日历的只读属性
    获取元素的id、id值，或者class、class值定位日历
    '''
    if index == None:
        index = 1
    if by == 'id':
        by_key = 'getElementById'
        js = "document.{}('{}').removeAttribute('readonly');".format(by_key, value)
    else:
        by_key = 'getElementsByClassName'
        js = "document.{}('{}')[{}].removeAttribute('readonly');".format(by_key, value, index)
    driver.execute_script(js)  # 执行js语句


def calendar_send(br, by, value, data, index=None):
    '''
    操作日历控件（单个日期）
    :param br:传入的浏览器对象，需要加上.driver
    :param by:日历元素的定位方式，id或者class
    :param value:对应的id或者class的值
    :param data:需要输入的日期、时间
    :param index:多个class时的序号
    :return:
    '''
    driver = br.driver
    if index == None:
        index = 0
    if by == 'id':
        element = driver.find_element_by_id(value)
    else:
        element = driver.find_elements_by_class_name(value)[index]
    try:
        element.get_attribute('readonly')  # 获取元素只读属性
        js_excute_calendar(driver, by, value, index)
    except:
        pass
    element.clear()
    element.send_keys(data)
    ActionChains(driver).send_keys(Keys.ENTER).perform()  # 回车


def switch_alert(br, info, value=None):
    '''
    系统级弹窗
    :param br:浏览器对象，需要加上.driver
    :param info:确认或取消
    :param value:是否需要输入的值
    '''
    driver = br.driver
    windows_alert = driver.switch_to.alert
    if info == 'accept':
        if value == None:
            windows_alert.accept()  # 点击确定
        else:
            windows_alert.send_keys(value)
            windows_alert.accept()
    else:
        windows_alert.dismiss()  # 点击取消


def scroll_get_element(br, path, child, str_info):
    '''
    滑动页面到底部，并查找元素
    :param br: 浏览器对象，需要加上.driver
    :param path: 父级xpath路径
    :param child: 子级class值
    :param str_info: 子级文本内容
    '''
    driver = br.driver
    js = 'document.documentElement.scrollTop=100000;'
    t = True
    while t:
        element_list = br.driver.find_elements_by_xpath("{}".format(path))
        for element in element_list:
            title_name = element.find_element_by_class_name(child).text
            if str_info in title_name:
                element.click()
                t = False
                break  # 仅控制了for循环，没有控制while循环
        driver.execute_script(js)
        time.sleep(3)


def scroll_element(br, by, value):
    '''
    滑动页面直到获取到元素
    :param br:浏览器对象，需要加上.driver
    :param by:元素属性
    :param value:属性值
    '''
    driver = br.driver
    js = 'document.documentElement.scrollTop=100000;'
    t = True
    while t:
        element = get_element(br, by, value)
        if element != None:
            element.click()
            t = False
        else:
            driver.execute_script(js)
            time.sleep(3)






def get_element(br, by, value):
    element = None
    driver = br.driver
    try:
        if by == 'id':
            element = driver.find_element_by_id(value)
        elif by == 'name':
            element = driver.find_element_by_name(value)
        elif by == 'classname':
            element = driver.find_element_by_class_name(value)
        elif by == 'css':
            element = driver.find_element_by_css_selector(value)
        elif by == 'link_text':
            element = driver.find_element_by_link_text(value)
        else:
            element = driver.find_element_by_xpath(value)
    except:
        print('定位方式：{}，定位置{}，定位出现错误，没有定位成功'.format(by, value))
    return element


def get_elements(br, by, value):
    elements = None
    driver = br.driver
    if by == 'id':
        elements = driver.find_elements_by_id(value)
    elif by == 'name':
        elements = driver.find_elements_by_name(value)
    elif by == 'class':
        elements = driver.find_elements_by_class_name(value)
    elif by == 'css':
        elements = driver.find_elements_by_css_selector(value)
    elif by == 'link_text':
        elements = driver.find_elements_by_link_text(value)
    else:
        elements = driver.find_elements_by_xpath(value)
    return elements


def get_level_element(br, by, value, node_by, node_value):
    element = get_element(br, by, value)
    if node_by == 'id':
        node_element = element.find_element_by_id(node_value)
    elif node_by == 'name':
        node_element = element.find_element_by_name(node_value)
    elif node_by == 'classname':
        node_element = element.find_element_by_class_name(node_value)
    elif node_by == 'css':
        node_element = element.find_element_by_css_selector(node_value)
    elif node_by == 'link_text':
        node_element = element.find_element_by_link_text(node_value)
    else:
        node_element = element.find_element_by_xpath(node_value)
    return node_element


def get_list_element(br, by, value, index):
    elements = get_elements(br, by, value)
    if index > len(elements):
        return None
    return elements[index]


def send_value(br, by, value, key):
    element = get_element(br, by, value)
    if element != None:
        element.send_keys(key)
    else:
        print('输入失败，定位元素没找到')
