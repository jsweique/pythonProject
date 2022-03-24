from login import Login
from event_add import EventAdd
from event_handle import EventHandle
from 我的事件处理记录 import MyEvents
from 新增资源 import Element

'''
# 登录
login = Login('http://47.102.147.120:2020/', '10000', '111111')
login.login()

# 新增事件,并接收事件编号、事件名称
code, name = EventAdd(login).event_add()
print(code)
print(name)
login.driver.close()

# 处置部门账号登录，处置事件
login = Login('http://47.102.147.120:2020/', 'pcjdpcs', '123456')
login.login()
EventHandle(login, code, name).event_handle()
login.driver.close()

# 我的事件处置记录查询
login = Login('http://47.102.147.120:2020/', 'pcjdpcs', '123456')
login.login()
MyEvents(login, code).my_events()
login.driver.close()
'''

# 新增标准地址
login = Login('http://192.168.20.214:10001/', '10000', '111111')
login.login()
MyEvents(login, '123456789').my_events()
