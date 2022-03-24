# from WorkPortal.Gulou.business.登录_business_song import LoginBusiness
# from WorkPortal.Gulou.business.用户中心_角色管理_business import Role
# from WorkPortal.Gulou.business.业务门户_日历_business import Calendar
from time import sleep

from zuoye.zuoyeAll.one.WorkPortal.Gulou.business.业务门户_日历_business import Calendar
from zuoye.zuoyeAll.one.WorkPortal.Gulou.business.用户中心_角色管理_business import Role
from zuoye.zuoyeAll.one.WorkPortal.Gulou.business.登录_business_song import LoginBusiness

Login = LoginBusiness(r'http://192.168.20.243:9083/login?redirect=%2Fconsole','jswq168','xsw2CDE#168')
Login.login()

Test=Role(Login,'用户中心')
Test.switch_Menu()

Test.role_Add()#新增_查询角色
Test.role_Edit()#编辑_查询角色

Test.role_Authorize_menu()#菜单配置
Test.role_Authorize_screen()#大屏导航配置
Test.role_Authorize_app()#APP配置
Test.role_Authorize_sys()#应用配置

Test.role_Delete()#清除已配置的权限，删除角色

print("test_用户中心_角色_新增_编辑_授权_删除，完成")
sleep(1)
print("--------------------------------------------------------------------------------")

#登录后测试日历的新增，编辑，删除
Test = Calendar(Login)
Test.add_Calendar()
Test.edit_Calendar()
Test.delete_Calendar()

print("test_业务门户_日历_新增_编辑_删除，完成")
sleep(1)
print("--------------------------------------------------------------------------------")

#退出登录
Login.close()