from login import Login
from peixianManagementSystem.assessmentPoints.demo.积分汇总 import PointsSummary
from peixianManagementSystem.assessmentPoints.demo.积分记录 import PointsRecord
from peixianManagementSystem.assessmentPoints.demo.规则设置 import RuleSettings

login = Login('http://192.168.20.214:10001/', '10000', '111111')
login.login()

# r = RuleSettings(login)
# r.add_rule()  # 新增考核规则
# r.edit_rule()  # 编辑考核规则
# r.disable_rule()  # 禁用考核规则

# p1 = PointsSummary(login)
# p1.query_point()#积分汇总查询


p2 = PointsRecord(login)
p2.query_points()  # 积分记录查询
