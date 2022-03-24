from WorkPortal.Gulou.business.登录_business_song import LoginBusiness
from WorkPortal.Gulou.business.业务门户_日历_business import Calendar
#登录测试
Login = LoginBusiness(r'http://192.168.20.243:9083/login?redirect=%2Fconsole','jswq168','xsw2CDE#168')
Login.login()

#登录后测试日历的新增，编辑，删除
Test = Calendar(Login)
Test.add_Calendar()
Test.edit_Calendar()
Test.delete_Calendar()

print("test_日历_新增_编辑_删除，完成")

#退出登录
Login.close()

