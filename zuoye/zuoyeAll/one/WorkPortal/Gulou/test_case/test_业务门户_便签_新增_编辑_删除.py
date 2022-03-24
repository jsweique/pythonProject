from WorkPortal.Gulou.business.登录_business_song import LoginBusiness
from WorkPortal.Gulou.business.业务门户_便签_business import shouye

login = LoginBusiness(r'http://192.168.20.243:9083/login?redirect=%2Fconsole', 'jswq168', 'xsw2CDE#168')
login.login()

s = shouye(login)
a = ['便签内容01', '便签内容02']
for i in a:
    s.add_shouye(i)
s.edit_shouye(a[0])
s.delete_shouye(a[1])

login.close()