from workportal.gulou.business.流程_快速链接_增改 import Quicklinks
from workportal.gulou.business.登录_快速链接 import BusinessCenter

login = BusinessCenter(r'http://221.229.205.205:9002/login?redirect=%2Fconsole', 'jswq168', 'qwe0jiangsuweique2022')
login.login_business_center()

a = Quicklinks(login)
b = ['快速链接03', '快速链接04']
for i in b:
    a.add_quick_links(i)

a.edit_quick_links(b[0])
a.delete_quick_links(b[1])

login.close_web()

