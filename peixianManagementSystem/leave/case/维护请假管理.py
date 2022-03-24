from login import Login
from peixianManagementSystem.leave.demo.我的请假申请 import MyLeave
from peixianManagementSystem.leave.demo.请假审批 import ApproveLeave
from peixianManagementSystem.leave.demo.请假管理 import LeaveManagement

login = Login('http://192.168.20.214:10001/', '10000', '111111')
login.login()
# l = LeaveManagement(login)
# l.add_leave_management()  # 新增请假类型
# #l.query_leave_management()  # 查询创建的请假类型
# l.edit_leave_management()   #编辑刚创建的请假类型
# l.delete_leave_management() #删除刚创建的请假类型

# s = MyLeave(login)
# s.add_my_leave()  # 新增请假申请
# s.edit_my_leave()  # 修改请假申请
# s.revoke_my_leave()  # 撤销请假

a = ApproveLeave(login)
a.approve_leave()  # 审批请假
