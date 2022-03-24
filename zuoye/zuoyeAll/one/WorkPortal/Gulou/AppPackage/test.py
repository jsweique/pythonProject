import time
# print (time.time())
a = str(time.strftime("%Y%m%d %H:%M:%S",time.localtime(time.time())))
print(a)