import unittest
import warnings

# from WorkPortal.Gulou.business.登录_business import Login
# from WorkPortal.Gulou.business.业务门户_快速链接_business import Home
#
# from WorkPortal.Gulou.config.browser import Browser
# from WorkPortal.Gulou.data.testdata import get_csv_data
from zuoye.test.test_log.decora import decoratore
from zuoye.zuoyeAll.one.WorkPortal.Gulou.business.业务门户_快速链接_business import Home
from zuoye.zuoyeAll.one.WorkPortal.Gulou.business.登录_business import Login
from zuoye.zuoyeAll.one.WorkPortal.Gulou.config.browser import Browser
from zuoye.zuoyeAll.one.WorkPortal.Gulou.data.testdata import get_csv_data


class TestLogin(unittest.TestCase):
    # 声明csv文件
    # 类属性
    # 注意:!!!! 数据路径  不一样！！！
    csv_file=r"D:\xyProject\WorkPortal\Gulou\data\account_login_gulou.csv"
    # 测试用例运行之前的准备工作
    def setUp(self):
        print("开始测试~~~~~~")
        # 忽略下警告
        warnings.simplefilter("ignore",ResourceWarning)
    # 测试用例运行的结束工作
    def tearDown(self) :
        print("结束测试！！！！！！")

    @decoratore
    def test_login_111(self):
        print("第一条预期成功用例测试----------")
        # 使用测试数据执行测试业务
        data=get_csv_data(self.csv_file,1)  #用文件csv_file 的 第2行
        br = Browser(data[0])  #第1个数据
        br.browser()
        Login(br).login(data[1],data[2])  #第2个  第3个
        #下面为调用方法，如在这个框架内修改，上面的文件不需要动
        Home(br).quick_links_add()  # 新增
        Home(br).quick_links_click()  #验证链接
        result =Home(br).quick_links_edit()  #编辑
        result1 = Home(br).quick_links_delete()  #删除
        # 使用断言产出测试结果
        self.assertTrue(result,result1)
        # br.driver.close()

# 测试执行器
if  __name__=='__main__':
    unittest.main()