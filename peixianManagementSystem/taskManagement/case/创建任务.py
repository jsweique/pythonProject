from login import Login
from peixianManagementSystem.taskManagement.demo.考核任务管理 import TaskManagement

login = Login('http://192.168.20.214:10001/', '10000', '111111')
login.login()

t = TaskManagement(login)
t.add_task()  # 新增任务
t.disable_task()  # 禁用任务
t.edit_task()  # 编辑任务
