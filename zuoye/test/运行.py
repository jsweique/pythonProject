import datetime
import time

from zuoye.test.test_log.decora import decoratore
from zuoye.test.全局变量 import OverallSituationTest
# from zuoye.workportal.gulou.config.窗口切换 import WindowSwitch
# from zuoye.workportal.gulou.business.角色管理 import RoleManagement
#from zuoye.workportal.test.全局变量 import OverallSituationTest

# o=OverallSituationTest(r'http://192.168.20.243:9083/login?redirect=%2Fconsole', 'jswq168', 'xsw2CDE#168')
# o.overall_situation_test()
# o.test_login()
#
# w=WindowSwitch(o)
# w.swtich_last('用户中心')
#
# r=RoleManagement(o)
# r.authorization_role()


class StartTest:
   @decoratore
   def start(self):
      self.driver='5'
      print("666")
      a = 1/0
      print(a)
      print('77777')

# StartTest().start()

def test03(*args):
   #print(args)
   for i in args:
      print(i)

a=1
b=2
c=3
test03()


