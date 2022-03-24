import asyncio
import os
import time

import aiofiles
import aiohttp
import requests
from lxml import etree

# async def down_file(resp):
#     #resp.encoding = 'utf-8'
#     et = etree.HTML(resp)
#     title = et.xpath("//div[@class='reader_box']/div[@class='title']/div[@class='title_txtbox']/text()")[0]
#     content = et.xpath("//div[@class='reader_box']/div[@class='content']//p/text()")
#     content = '\n'.join(content)
#     async with aiofiles.open('./novel' + title, mode='w') as w:
#         await w.write(content)

semaphore = asyncio.Semaphore(100)  # 控制select打开文件数量，window默认是509，超过就会报异常


def add_chaper(url, header):
    resp = requests.get(url, headers=header)
    resp.encoding = 'utf-8'
    etr=etree.HTML(resp.text)
    et = etr.xpath("//div[@class='volume-list']/div/div/text()")
    temp = []
    for i in et:
        if not i.startswith(' ') and not i.startswith('\r\n'):
            temp.append(i)
    for i in temp:
        if not os.path.exists('./novel/'+i):
            os.makedirs('./novel/'+i)


async def get_url(href):
    print('开始下载')
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(href) as resp:
                page_source = await resp.text()
                # print(page_source)
                et = etree.HTML(page_source)
                chapter = et.xpath(
                    "//div[@class='readerPageWrap']/div[@class='rw_3']/div[@class='reader_crumb']/text()")[-1]

                c = chapter.replace(' > ', '')

                # path = '../pythonProject/reptile_01/novel/' + c
                # isExists = os.path.exists(path)
                # # print(isExists)
                # if not isExists:
                #     os.makedirs(path)

                title = et.xpath("//div[@class='reader_box']/div[@class='title']/div[@class='title_txtbox']/text()")[
                    0].strip()
                content = et.xpath("//div[@class='reader_box']/div[@class='content']//p/text()")
                content = '\n'.join(content)
                async with aiofiles.open('./novel/{}/{}.txt'.format(c, title), mode='w', encoding='utf-8') as w:
                    await w.write(content)
    print('下载完成')


async def get_href_list(url, header):
    resp = requests.get(url, headers=header)
    resp.encoding = 'utf-8'
    # print(resp.text)
    # print(resp.text)
    et = etree.HTML(resp.text)
    href_list = et.xpath("//div[@class='volume-list']/div/ul[@class='chapter-list clearfix']/li/a/@href")
    print(href_list)
    tasks = []
    for href in href_list:
        t = asyncio.create_task(get_url(href))
        tasks.append(t)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    url = 'http://book.zongheng.com/showchapter/236761.html'
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Host": "book.zongheng.com",
        "Cookie": "BAIDU_SSP_lcr=https://www.baidu.com/link?url=TC_gBjNE3g9TRIbAN62wSg3nQtH0E7odMHlIPOya-9UhPjn2I0CTywGzMM0zPxLH&wd=&eqid=ec57b4fa00036daa000000056196fba8; ZHID=1637284787713ZHFEKK5IFOE3FJMED01; zh_visitTime=1637284787714; zhffr=www.baidu.com; Hm_lvt_c202865d524849216eea846069349eb9=1637284788; Hm_up_c202865d524849216eea846069349eb9=%7B%22uid_%22%3A%7B%22value%22%3A%221637284787713ZHFEKK5IFOE3FJMED01%22%2C%22scope%22%3A1%7D%7D; ver=2018; sajssdk_2015_cross_new_user=1; v_user=http%3A%2F%2Fhao123.zongheng.com%2F%7Chttp%3A%2F%2Fbook.zongheng.com%2Fshowchapter%2F165799.html%7C95627127; JSESSIONID=abcPAY1xyu08reFX3X10x; PassportCaptchaId=e0987c9a2c0c8e51669dfd879127f509; rSet=1_3_1_14; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d35c755471fa-0efe950dfce68b-a7d193d-2359296-17d35c75548dd8%22%2C%22%24device_id%22%3A%2217d35c755471fa-0efe950dfce68b-a7d193d-2359296-17d35c75548dd8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; platform=H5; AST=1637296734606ab5b537ced; Hm_lpvt_c202865d524849216eea846069349eb9=1637291502"
    }
    # asyncio.run(get_href_list(url, header))

    add_chaper(url, header)#创建章节文件夹
    time.sleep(1)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_href_list(url, header))
    loop.close()
