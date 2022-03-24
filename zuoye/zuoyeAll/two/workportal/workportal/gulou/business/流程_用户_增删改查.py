import time

import ddddocr
from PIL import Image


class Systemuser:  #定义用户管理
  def __init__(self,loginname,fullname,phonenumber,idnumber,driver):  #定义属性
    self.login = driver
    self.loginname = loginname
    self.fullname = fullname
    self.phonenumber = phonenumber
    self.idnumber = idnumber



  def add_user(self): #新增用户
    time.sleep(2)
    self.login.driver.find_element_by_class_name('el-button--success').click()
    time.sleep(3)
    self.login.driver.find_element_by_xpath("//input[@placeholder='登录名']").send_keys(self.loginname)
    time.sleep(1)
    self.login.driver.find_element_by_xpath("//input[@placeholder='姓名']").send_keys(self.fullname)
    time.sleep(1)
    self.login.driver.find_element_by_xpath("//input[@placeholder='手机号']").send_keys(self.phonenumber)
    time.sleep(1)
    self.login.driver.find_element_by_xpath("//input[@placeholder='身份证号']").send_keys(self.idnumber)
    time.sleep(2)
    self.login.driver.find_element_by_xpath(
      '/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[5]/div[1]/div[2]/form[1]/div[4]/div[1]/div[1]/div[1]/button[1]').click() #定义所属区域下拉框
    time.sleep(3)
    self.login.driver.find_element_by_xpath(
      '/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/label[1]/span[1]/span[1]').click() #选择区域
    time.sleep(3)
    self.login.driver.find_element_by_xpath('//div[3]//div[1]//div[3]//div[1]//button[1]').click() #选择区域
    time.sleep(2)
    self.login.driver.find_element_by_xpath(
      '/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[5]/div[1]/div[2]/form[1]/div[5]/div[1]/div[1]/div[2]/span[1]/span[1]/i[1]').click() #定义平台角色下拉框
    time.sleep(3)
    self.login.driver.find_elements_by_xpath("//span[contains(text(),'平台管理员')]")[7].click()  #选择角色
    time.sleep(3)
    self.login.driver.find_elements_by_xpath("//span[contains(text(),'新增平台用户')]")[1].click() #点击新增平台用户收回弹窗
    time.sleep(3)
    self.login.driver.find_element_by_xpath(
      '/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[5]/div[1]/div[2]/form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/i[1]') .click()#选择部门，输入部门
    time.sleep(3)
    self.login.driver.find_elements_by_xpath("//span[contains(text(),'鼓楼区指挥中心')]")[1].click()   #选择部门
    time.sleep(2)
    self.login.driver.find_element_by_xpath(" // span[contains(text(), '确认')]").click()  #点击确定，提交
    time.sleep(2)
    try:
        t = self.login.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]").text
        if t == '保存成功':
            print('【系统用户】 新增成功！')
            print('-------------------------------------')
        else:
            print('【系统用户】 新增失败！！')
            print('------------------------------------- ')

    except:
        print('未获取到新增用户提示！')
    time.sleep(1)


  def search(self):  #查询用户
    self.login.driver.find_element_by_xpath("//input[@placeholder='请输入登录名、姓名、手机号或身份证号']").send_keys(self.loginname)
    time.sleep(2)
    self.login.driver.find_elements_by_xpath("//button[contains(@class,'el-button el-button--primary el-button--mini')]")[0].click()
    time.sleep(2)
    txt = self.login.driver.find_elements_by_xpath("//div[contains(text(),'{}')]".format(self.fullname))[0].text #验证用户查询
    time.sleep(3)
    print('【系统用户】 查询成功！'+txt)
    print('------------------------------------- ')
    self.login.driver.find_elements_by_xpath("//span[contains(text(),'重置')]")[0].click()
    time.sleep(3)



  def edit(self):  # 编辑用户
    self.login.driver.find_element_by_xpath("//div[contains(@class,'el-table__fixed-right')]//button[2]").click()
    time.sleep(2)
    self.login.driver.find_element_by_xpath("//input[@placeholder='登录名']").clear()
    time.sleep(2)
    self.login.driver.find_element_by_xpath("//input[@placeholder='登录名']").send_keys('1998')
    time.sleep(3)
    self.login.driver.find_element_by_xpath("//input[@placeholder='姓名']").clear()
    time.sleep(2)
    self.login.driver.find_element_by_xpath("//input[@placeholder='姓名']").send_keys('苏琪')
    time.sleep(2)
    self.login.driver.find_element_by_xpath(
        '/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[5]/div[1]/div[3]/div[1]/button[1]/span[1]').click()
    time.sleep(3)
    try:
        tt= self.login.driver.find_element_by_xpath("//p[contains(text(),'保存成功')]").text
        if tt == '保存成功':
            print('【系统用户】 修改编辑成功！')
            print('------------------------------------- ')
        else:
            print('【系统用户】 修改编辑失败！！')
            print('------------------------------------- ')
    except:
        print('未获取到编辑用户提示！')



  def edit_search(self):#编辑用户再次查询用户
    self.login.driver.find_element_by_xpath("//input[@placeholder='请输入登录名、姓名、手机号或身份证号']").send_keys('1998')
    time.sleep(2)
    self.login.driver.find_elements_by_xpath(
    "//button[contains(@class,'el-button el-button--primary el-button--mini')]")[0].click()
    time.sleep(2)
    txt = self.login.driver.find_elements_by_xpath("//div[contains(text(),'苏琪')]")[ 0].text  # 验证用户查询
    time.sleep(3)
    print('【系统用户】 编辑后查询成功！' + txt)
    print('------------------------------------- ')
    self.login.driver.find_elements_by_xpath("//span[contains(text(),'重置')]")[0].click()
    time.sleep(3)



  def quit(self): #退出用户
    self.login.driver.find_element_by_xpath("//img[@class='user-avatar']").click()
    time.sleep(2)
    self.login.driver.find_element_by_xpath('/html[1]/body[1]/ul[1]/span[2]/li[1]').click()
    time.sleep(2)
    self.login.driver.find_elements_by_xpath("//span[contains(text(),'确定')]")[3].click()
    time.sleep(3)
    if self.login.driver.title =='登录 - 智慧鼓楼工作门户':
      print('【系统用户】 系统管理员退出成功！')
      print('------------------------------------- ')
    else:
      print('【系统用户】 系统管理员退出失败！！')
      print('-------------------------------------')


  def user_logion(self,name,password): #验证新用户登录
          self.login.driver.find_element_by_xpath("//input[@placeholder='账号']").clear()
          time.sleep(2)
          self.login.driver.find_element_by_xpath( "//input[@placeholder='账号']").send_keys(name)
          time.sleep(2)
          self.login.driver.find_element_by_xpath("//input[@placeholder='密码']").clear()
          time.sleep(2)
          self.login.driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys(password)
          time.sleep(2)

          self.login.driver.save_screenshot(r"C:\yanzhengma\photo0003.png")
          code =self.login.driver.find_element_by_xpath("//div[@class='login-code']")
          location =code.location
          size =code.size

          img = (int(location['x'] + 340), int(location['y'] + 146),
                 int(location['x'] + size['width'] + 380),
                 int(location['y'] + size['height'] + 152))

          i = Image.open(r"C:\yanzhengma\photo0003.png").crop(img)
          i.save(r"C:\yanzhengma\photo0004.png")

          ocr = ddddocr.DdddOcr()  #第三方处理验证码
          with open(r"C:\yanzhengma\photo0004.png", 'rb') as f:
              img_bytes = f.read()
          t = ocr.classification(img_bytes)
          self.login.driver.find_element_by_xpath(
            '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[2]/input[1]').clear()
          self.login.driver.find_element_by_xpath(
            '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/div[1]/div[1]/div[2]/input[1]').send_keys(t)
          time.sleep(3)
          self.login.driver.find_element_by_xpath(
            '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[5]/div[1]/button[1]/span[1]/span[1]').click()
          time.sleep(3)
          try:
              if self.login.driver.title == '个人工作台 - 智慧鼓楼工作门户':  #判断标题
                print('【系统用户】 新增用户登录成功！')
                print('------------------------------------- ')
              else:
                print('【系统用户】 新增用户登录失败，再次登录！')
                print('------------------------------------- ')
          except:
              print('未获取到网页标题')




  def  user_center(self):#登录管理员应用中心
      self.login.driver.find_element_by_xpath("//div[@class='el-row']//li[7]").click()
      time.sleep(3)
      self.login.driver.find_elements_by_xpath("// h4[contains(text(), '用户中心')]")[0].click()
      time.sleep(3)

  def user_window(self):  # 切换窗口用户管理页面
      windows = self.login.driver.window_handles
      self.login.driver.switch_to.window(windows[-1])  # 切换到当前窗口
      time.sleep(2)
      self.login.driver.find_element_by_xpath(
          '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/div[3]/li[1]/div[1]').click()
      time.sleep(2)
      self.login.driver.find_element_by_xpath(
          '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/div[3]/li[1]/ul[1]/div[1]/a[1]/li[1]').click()
      time.sleep(2)

  def user_quit(self): #退出用户管理
    time.sleep(2)
    self.login.driver.find_element_by_xpath("//a[contains(text(),'退出')]").click()
    time.sleep(3)
    self.login.driver.find_element_by_xpath("//span[contains(text(),'确定')]").click()
    time.sleep(2)
    try:
        if self.login.driver.title == '个人工作台 - 智慧鼓楼工作门户':  # 判断标题
            print('【系统用户】 新用户登录成功！')
            print('------------------------------------- ')
        else:
            print('【系统用户】 新用户登录失败，再次登录！')
            print('------------------------------------- ')
    except:
        print('未获取到网页标题！')


  def delete(self): #删除用户
      self.login.driver.find_element_by_xpath("//input[@placeholder='请输入登录名、姓名、手机号或身份证号']").send_keys('苏琪')
      time.sleep(2)
      self.login.driver.find_elements_by_xpath("//button[contains(@class,'el-button el-button--primary el-button--mini')]")[0].click()
      time.sleep(2)
      self.login.driver.find_element_by_xpath(
          '/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[6]/div[5]/div[2]/table[1]/tbody[1]/tr[1]/td[16]/div[1]/button[4]/span[1]').click()
      time.sleep(2)
      self.login.driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[3]/button[2]/span[1]').click()
      time.sleep(2)
      try:
        ttt = self.login.driver.find_element_by_xpath('//p[contains(text(),"删除成功")]').text
        if ttt == '删除成功':
            print('【系统用户】 新增用户删除成功！')
            print('------------------------------------')
        else:
            print('【系统用户】 新增用户删除失败！！')
            print('-------------------------------------')
      except:
          print('未获取到删除用户提示')


  def first_page(self):  #个人中心

      self.login.driver.find_element_by_xpath('//body//li[1]').click()
      time.sleep(3)


  def browser_close(self):
      win = self.login.driver.window_handles
      self.login.driver.switch_to.window(win[-1])  # 切换到当前窗口
      self.login.driver.close() # 关闭当前窗口
      self.login.driver.switch_to_window(win[0])  # 切换回业务中台窗口

















