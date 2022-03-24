# from WorkPortal.Gulou.business.业务中台登录页_business import LoginBusinessCenter
# from WorkPortal.Gulou.business.用户中心_角色管理_business import Role
# from WorkPortal.Gulou.business.便签界面_business import shouye
from zuoye.zuoyeAll.three.WorkPortal.Gulou.business.业务中台登录页_business import LoginBusinessCenter
from zuoye.zuoyeAll.three.WorkPortal.Gulou.business.便签界面_business import shouye
from zuoye.zuoyeAll.three.WorkPortal.Gulou.business.用户中心_角色管理_business import Role

login = LoginBusinessCenter('http://192.168.20.243:9083/login?redirect=%2Fconsole', 'jswq168', 'xsw2CDE#168')
login.login_bussiness_center()

Role(login).switch_window() #切换窗口
Role(login).switch_menu() #进入角色管理
Role(login).role_add() #新增角色名称
Role(login).role_query() #查询角色
Role(login).role_edit() #编辑角色
Role(login).role_authorization() #授权角色
Role(login).role_delete() #删除角色

login.driver.close() #关闭当前窗口
login.driver.switch_to.window(login.driver.window_handles[0]) #返回第一个窗口

s = shouye(login)
a = ['便签内容01', '便签内容02']
for i in a:
    s.add_shouye(i)
s.edit_shouye(a[0])
s.delete_shouye(a[1])

login.driver.close()