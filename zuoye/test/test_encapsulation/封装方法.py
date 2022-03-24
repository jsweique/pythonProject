from selenium import webdriver

driver = webdriver.Chrome()


def get_element(by, value):
    element = None
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
        print('定位方式：{}，定位置{}，定位出现错误，没有定位成功'.format(by,value))
    return element

def get_elements(by, value):
    elements = None
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

def get_level_element(by,value,node_by,node_value):
    element = get_element(by,value)
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

def get_list_element(by,value,index):
    elements=get_elements(by,value)
    if index > len(elements):
        return None
    return elements[index]

def send_value(by,value,key):
    element=get_element(by,value)
    if element != None:
        element.send_keys(key)
    else:
        print('输入失败，定位元素没找到')



