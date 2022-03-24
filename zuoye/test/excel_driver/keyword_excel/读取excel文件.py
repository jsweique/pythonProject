import openpyxl

from zuoye.test.excel_driver.web_keys.web_ui import WebDemo

'''
excel文件的读取流程：
    1、打开excel
    2、获取指定的sheet页
    3、读取当前指定sheet页中的内容
'''

# 打开excel，读取工作簿，excel不能在pycharm中创建，需要在文件夹中创建
excel = openpyxl.load_workbook(
    r'C:\Users\zheng\PycharmProjects\pythonProject\zuoye\test\excel_driver\test_cases\test_cases_demo.xlsx')
# 指定需要的sheet页
# sheet = excel['Sheet1']
# 获取多个sheet页
sheets = excel.sheetnames  # 所有sheet页名称
for i in sheets:
    sheet = excel[i]
    for values in sheet.values:
        parms = {}
        parms['name'] = values[2]
        parms['value'] = values[3]
        parms['txt'] = values[4]
        # 结合文件来判断
        if type(values[0]) is int:
            if values[1] == 'browser':
                wd = WebDemo(parms['txt'])
            else:
                getattr(wd, values[1])(**parms)  # 反射：wd是类对象，第二个参数是字符串匹配的类中方法
        else:
            pass
