# from workportal.gulou.business.流程_快速链接_增改 import Quicklinks
# from workportal.gulou.business.流程_用户_增删改查 import Systemuser
# from workportal.gulou.business.登录_用户管理中心 import BusinessCenter



#登录用户管理--增删改查
from zuoye.zuoyeAll.two.workportal.workportal.gulou.business.流程_快速链接_增改 import Quicklinks
from zuoye.zuoyeAll.two.workportal.workportal.gulou.business.流程_用户_增删改查 import Systemuser
from zuoye.zuoyeAll.two.workportal.workportal.gulou.business.登录_用户管理中心 import BusinessCenter

login = BusinessCenter(r'http://192.168.20.243:9083/login?redirect=%2Fconsole', 'jswq168', 'xsw2CDE#168')
login.login_business_center() #登录业务中台
login.application_center()  #切换应用中心
login.new_window()         #切换系统用户

user = Systemuser(r'jswq管理员','苏苏 ','15996266682', '110101197701010113',login)
user.add_user()  #新增用户
user.search()    #查询用户
user.edit()      #修改编辑用户
user.edit_search() #编辑后查询用户
user.quit()       #退出用户
user.user_logion(r'1998','GLabc123')  #新用户登录验证
user.user_quit()  #新用户退出
user.user_logion(r'jswq168', 'xsw2CDE#168') #登录系统管理员
user.user_center() #应用中心
user.user_window()#用户管理
user.delete() #删除新用户
user.browser_close() #关闭当前浏览器
user.browser_close()#关闭当前浏览器
user.first_page() #切换个人工作台



#快速链接
a = Quicklinks(login)
b = ['快速链接03', '快速链接04']
for i in b:
    a.add_quick_links(i)

a.edit_quick_links(b[0])
a.delete_quick_links(b[1])

login.close_web()










