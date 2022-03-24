#!/usr/bin/env python
# encoding: utf-8
import datetime
import os
import time
from functools import wraps
import traceback

from PIL import ImageGrab

from zuoye.test.test_log.log import get_logger

log_dir1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
today = time.strftime('%Y%m%d', time.localtime(time.time()))
full_path = os.path.join(log_dir1, today)
if not os.path.exists(full_path):
    os.makedirs(full_path)
img_path = full_path + "{}.jpg".format(time.strftime("%H%M%S", time.localtime()))


# 在这里引用wraps,一个装饰器的装饰器，目的为了保持引用进来的函数名字不发生变化
def decoratore(func):
    @wraps(func)
    def log(*args, **kwargs):
        try:
            print("当前运行方法", func.__name__)
            return func(*args, **kwargs)
        except Exception as e:
            get_logger().error("{} is error,here are details:{}".format(func.__name__, traceback.format_exc()))
            im = ImageGrab.grab()
            im.save(img_path)

    return log
