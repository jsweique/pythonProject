from zuoye.workportal.gulou.business.业务中台登录 import LoginBusinessCenter
from zuoye.workportal.gulou.business.业务中心_工作日历_business import ShopCalendar
from zuoye.workportal.gulou.config.窗口切换 import WindowSwitch
from zuoye.workportal.gulou.business.用户中心_部门管理_business import DepartmentManagement

login = LoginBusinessCenter(r'http://192.168.20.243:9083/login?redirect=%2Fconsole', 'jswq168', 'xsw2CDE#168')
login.login_bussiness_center()

win = WindowSwitch(login)
win.swtich_last('用户中心')

depart = DepartmentManagement(login)
result_add_type_management = depart.add_type_management()  # 新增类型
result_query_type_management = depart.query_type_management()  # 查询类型
result_edit_type_management = depart.edit_type_management()  # 编辑类型
result_add_functional_management = depart.add_functional_management()  # 新增职能
result_query_functional_management = depart.query_functional_management()  # 查询职能
result_edit_functional_management = depart.edit_functional_management()  # 编辑职能
result_add_department = depart.add_department()  # 新增部门
result_query_department = depart.query_department()  # 查询部门
result_edit_department = depart.edit_department()  # 编辑部门
result_delete_department = depart.delete_department()  # 删除部门
result_delete_functional_management = depart.delete_functional_management()  # 删除职能
result_delete_type_management = depart.delete_type_management()  # 删除类型
print('新增类型返回结果：{}；\n查询类型返回结果：{}；'.format(result_add_type_management, result_query_type_management))
print('编辑类型返回结果：{}；\n新增职能返回结果：{}；'.format(result_edit_type_management, result_add_functional_management))
print('查询职能返回结果：{}；\n编辑职能返回结果：{}；'.format(result_query_functional_management, result_edit_functional_management))
print('新增部门返回结果：{}；\n查询部门返回结果：{}；'.format(result_add_department, result_query_department))
print('编辑部门返回结果：{}；\n删除部门返回结果：{}；'.format(result_edit_department, result_delete_department))
print('删除职能返回结果：{}；\n删除类型返回结果：{}；'.format(result_delete_functional_management, result_delete_type_management))


login.close_web()
win.switch_first()
s = ShopCalendar(login)
a = ['事件标题01', '事件标题02']
for i in a:
    s.add_shopCalendar(i)
s.edit_shopCalendar(a[0])
s.delete_shopCalendar(a[1])

login.close_web()
