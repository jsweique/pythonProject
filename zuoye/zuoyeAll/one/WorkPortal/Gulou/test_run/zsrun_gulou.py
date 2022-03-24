import sys

# 项目路径
# 项目上右击　copy  path
from Peixian.test_run.BSTestRunner import BSTestRunner

path=r'E:\DispatchingPlatform\Gulou'
sys.path.append(path)

import unittest
import time
#指定测试用例和测试报告的路径
test_dir = '../test_case'
report_dir = '../reports'  #指定测试报告
#匹配测试多条用例
# 代表执行 以test_开头的所有文件
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
#定义报告的文件格式
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + ' test_report.html'
#运行用例并生成测试报告
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title="zs的测试报告", description="zs的测试报告描述：")
    runner.run(discover)