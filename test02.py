import asyncio
import os
import threading
from multiprocessing import Process

# class Test02:
#     a = 1
#
#     def test03(self, m):
#         global a
#         b = Test02().a
#         for i in range(5):
#             b += 1
#             print('test03:', b)
#
#     def test04(self, n):
#         global a
#         b = Test02().a
#         for i in range(5):
#             b += 2
#             print('test04:', b)
#
#
# if __name__ == '__main__':
#     p1 = Process(target=Test02().test03, args=(1,))
#     p2 = Process(target=Test02().test04, args=(2,))
#     p1.start()
#     p2.start()
#     print('over')
from urllib import parse

import asserts as asserts

# def test03(m):
#     try:
#         m += 3
#         # print('m值是3')
#     except:
#         # print('m不是3')
#         return True
#     else:
#         return False

# finally:
# print('over')


# a = test03(4)
# assert True(a)
# print(a)
# asserts.assert_true(Test=a)


# 解析域名
# import socket
#
# result = socket.gethostbyname('47test.jsweique.com')
# print(result)
import requests
from lxml import etree

url = 'http://book.zongheng.com/chapter/473127/7840937.html'
proxy = {
    "http": "http://60.170.204.30:8060",
    "https": "https://60.170.204.30:8060"
}

header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Host": "book.zongheng.com",
    "Cookie": "BAIDU_SSP_lcr=https://www.baidu.com/link?url=TC_gBjNE3g9TRIbAN62wSg3nQtH0E7odMHlIPOya-9UhPjn2I0CTywGzMM0zPxLH&wd=&eqid=ec57b4fa00036daa000000056196fba8; ZHID=1637284787713ZHFEKK5IFOE3FJMED01; zh_visitTime=1637284787714; zhffr=www.baidu.com; Hm_lvt_c202865d524849216eea846069349eb9=1637284788; Hm_up_c202865d524849216eea846069349eb9=%7B%22uid_%22%3A%7B%22value%22%3A%221637284787713ZHFEKK5IFOE3FJMED01%22%2C%22scope%22%3A1%7D%7D; ver=2018; sajssdk_2015_cross_new_user=1; v_user=http%3A%2F%2Fhao123.zongheng.com%2F%7Chttp%3A%2F%2Fbook.zongheng.com%2Fshowchapter%2F165799.html%7C95627127; JSESSIONID=abcPAY1xyu08reFX3X10x; PassportCaptchaId=e0987c9a2c0c8e51669dfd879127f509; rSet=1_3_1_14; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d35c755471fa-0efe950dfce68b-a7d193d-2359296-17d35c75548dd8%22%2C%22%24device_id%22%3A%2217d35c755471fa-0efe950dfce68b-a7d193d-2359296-17d35c75548dd8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; platform=H5; AST=1637296734606ab5b537ced; Hm_lpvt_c202865d524849216eea846069349eb9=1637291502"
}
resp = requests.get(url,headers=header)
# print(resp.text)
resp.encoding = 'utf-8'
#print(resp.text)

et = etree.HTML(resp.text)
chapter=et.xpath("//div[@class='readerPageWrap']/div[@class='rw_3']/div[@class='reader_crumb']/text()")
c=chapter[-1]
print(c)
path='../pythonProject/reptile_01/novel/'+c.replace(' > ','')
isExists=os.path.exists(path)
print(isExists)
if not isExists:
    os.makedirs(path)
# for c in chapter:
#     # cc='\r\n'.join(c).strip()
#     print(c)
# title = et.xpath("//div[@class='reader_box']/div[@class='title']/div[@class='title_txtbox']/text()")[0]
# content = et.xpath("//div[@class='reader_box']/div[@class='content']//p/text()")
# content='\n'.join(content)
# print(title, content)

# s='     第八章 不知道的大凶险.   '
# print(s.strip())

src='https://www.baidu.com/'
path='/js/player'
src_url=parse.urljoin(src,path) #src path拼接在一起

#自省，如果下载失败，会重试（访问失败后进行重试）
for i in range(10):
    try:
        #协程执行的内容
        pass
        break
    except:
        print('下载出错')
        await asyncio.sleep((i+1)*5)    #可以适当的进行睡眠
        #添加的测试内容
