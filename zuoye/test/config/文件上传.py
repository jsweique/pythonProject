import time

import pyperclip
import win32api
import win32con
from pykeyboard import PyKeyboard  # 安装PyUserInput


class UploadFile:

    def upload_file(self, filePath):
        '''
        使用python的 win32api,win32con 模块按键输入，实现文件上传操作。
        :param webEle: 页面中上传文件按钮，是已经获取到的对象
        :param filePath: 要上传的文件地址，绝对路径
        :return:
        '''
        pyperclip.copy(filePath)  # 复制文件路径到剪切板
        time.sleep(3)
        win32api.keybd_event(17, 0, 0, 0)  # 发送ctrl(17) + V(87) 按钮
        win32api.keybd_event(86, 0, 0, 0)
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按钮
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
        win32api.keybd_event(13, 0, 0, 0)  # 回车
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开按钮

    def upload_file_py(self, filePath):
        '''
        无法输入中文路径
        :param filePath:
        :return:
        '''
        pykey = PyKeyboard()
        # pykey.tap_key(pykey.shift_key)#切换输入法
        pykey.type_string(filePath)  # 上传文件
        time.sleep(3)
        pykey.tap_key(pykey.enter_key)  # 回车
        time.sleep(1)
