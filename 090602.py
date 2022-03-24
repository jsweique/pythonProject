from selenium import webdriver
from PIL import Image
import pytesseract
import time


def tes(list):
    list1 = []
    for i in list:
        if i.isdigit():
            list1.append(i)
    return ''.join(list1)


def image(src):
    driver.save_screenshot(r"{}\photo0001.png".format(src))
    imgelement = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/form/div[3]/img')  # 定位验证码
    location = imgelement.location  # 获取验证码x,y轴坐标
    print(location)
    size = imgelement.size  # 获取验证码的长宽
    print(size)
    rangle = (int(location['x'] + 128), int(location['y'] + 175), int(location['x'] + size['width'] + 150),
              int(location['y'] + size['height'] + 185))  # 写成我们需要截取的位置坐标
    i = Image.open(r"{}\photo0001.png".format(src))  # 打开截图
    frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4 = frame4.convert('RGB')
    frame4.save(r"{}\photo0002.png".format(src))  # 保存我们接下来的验证码图片 进行打码
    # time.sleep(3)
    pytesseract.pytesseract.tesseract_cmd = 'C:/Tesseract-OCR/tesseract.exe'
    tessdata_dir_config = '--tessdata-dir "C:/Tesseract-OCR/tessdata"'
    image = Image.open(r"{}\photo0002.png".format(src))
    return image

driver = webdriver.Chrome()
driver.get(r'http://192.168.20.211:2030/')
driver.maximize_window()

image = image(r'C:\yanzhengma')
time.sleep(3)
list2 = list(pytesseract.image_to_string(image))
t = tes(list2)
print(t)

driver.close()