'''
抓取网站的图片
分析：进程1：从主页面当中解析出详情页的url，从详情页中提取到图片的下载地址
    进程2：把拿到的下载地址，进行下载
        队列：可以进行队列之间的通信
'''
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Queue
from urllib import parse

import requests
from lxml import etree


def get_img_src(q):
    url = "http://www.591mm.com/mntt/6.html"
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    tree = etree.HTML(resp.text)
    href_list = tree.xpath("//div[@class='MeinvTuPianBox']/ul/li/a[1]/@href")  # 拿到的只有后面的内容，需要拼接域名

    for href in href_list:
        href = parse.urljoin(url, href)  # 负责拼接url
        child_resp = requests.get(href)
        child_resp.encoding = 'utf-8'
        child_tree = etree.HTML(child_resp.text)
        try:
            src = child_tree.xpath("//div[@id='picBody']//img/@src")[0]
            print(src)
            q.put(src)  # 向队列中装东西
        except:
            print('未获取到内容')
    q.put('完事了')


def download(url):
    print('开始下载')
    name = url.split('/')[-1]
    with open('./img/' + name, mode='wb') as f:
        resp = requests.get(url)
        f.write(resp.content)
    print('下载完毕')


def downloag_img(q):
    with ThreadPoolExecutor(10) as t:   #创建线程池
        while 1:
            src = q.get()  # 从队列中获取数据，如果没有数据就会阻塞
            if src == '完事了':
                break
            t.submit(download, src)


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=get_img_src, args=(q,))
    p2 = Process(target=downloag_img, args=(q,))
    p1.start()
    p2.start()
