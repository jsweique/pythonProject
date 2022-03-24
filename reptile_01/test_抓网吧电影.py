import asyncio
import os
import re
from urllib import parse

import aiofiles
import aiohttp
import requests
from Crypto.Cipher import AES
from lxml import etree

'''
针对下载网吧电影的分析
1、拿到视频页的页面源代码
2、从视频页的页面源代码中找到对应的iframe，提取到iframe里面的src
3、请求到src对应的页面源代码，在该页面中解析出真正的m3u8文件地址
4、下载第一层m3u8，从第一层m3u8中解析出第二层的地址
5、下载第二层m3u8，从第二层m3u8中解析出每一个ts文件的路径，启动协程任务下载ts文件
6、对ts文件进行解密操作：先拿key（有些ts文件没有加密，可以直接播放）
7、对ts文件进行合并，还原回mp4文件
'''

semaphore = asyncio.Semaphore(100)


def get_page_source(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return resp.text


# 2、从视频页的页面源代码中找到对应的iframe，提取到iframe里面的src
def get_iframe_src(url):
    # 1、拿到视频页的页面源代码
    print('获取iframe的src值')
    page_source = get_page_source(url)
    # 2、从视频页的页面源代码中找到对应的iframe，提取到iframe里面的src
    etr = etree.HTML(page_source)
    src = etr.xpath("//iframe[@id='mplay']/@src")[0]
    src_url = parse.urljoin(url, src)
    print('成功获取iframe的src值', src_url)
    return src_url

#获取第一层m3u8地址
def get_first_m3u8_url(src_url):
    print('获取第一层m3u8地址')
    page_source = get_page_source(src_url)
    obj = re.compile(r'url: "(?P<m3u8>.*?)",', re.S)
    result = obj.search(page_source)
    m3u8_url = result.group('m3u8')
    print('成功获取到第一次m3u8地址')
    return m3u8_url


# 获取到第二层m3u8文件，并保存在硬盘中
def down_m3u8_file(first_m3u8_url):
    print('下载第二层m3u8地址')
    page_source = get_page_source(first_m3u8_url)
    second_m3u8_url = page_source.split()[-1]
    second_m3u8_url = parse.urljoin(first_m3u8_url, second_m3u8_url)
    # 下载第二层m3u8文件
    second_m3u8 = get_page_source(second_m3u8_url)
    with open('./movies/m3u8.txt', mode='w', encoding='utf-8') as w:
        w.write(second_m3u8)
    print('下载第二层m3u8地址...数据以保存在m3u8.txt文件中。。。')


# 下载单个ts文件
async def download_one(url):
    async with semaphore:
        for i in range(10):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as resp:
                        wb = await resp.content.read()
                        # print('wb:' + wb)
                        async with aiofiles.open('./movies/电影_源_加密前/{}'.format(url.split('/')[-1]), mode='wb') as w:
                            await w.write(wb)
                print('下载成功', url)
                break
            except:
                print("下载失败，出现错误", url)
                await asyncio.sleep((i + 1) * 5)

# 下载所有ts文件
async def download_all_ts():
    tasks = []
    with open('./movies/m3u8.txt', mode='r') as r:
        for f1 in r:
            if f1.startswith('#'):
                continue
            t = asyncio.create_task(download_one(f1.strip()))
            tasks.append(t)
    await asyncio.wait(tasks)


# 获取密钥
def get_key():
    obj = re.compile(r'URI="(?P<key_url>.*?)"', re.S)
    key_url = ''
    with open('./movies/m3u8.txt', mode='r', encoding='utf-8') as f:
        result = obj.search(f.read())
        key_url = result.group('key_url')
    # 请求到key的url，获取到真正的密钥
    key_str = get_page_source(key_url)
    return key_str.encode('utf-8')  # 返回密码的字节


# 创建协程解密（解密单个ts）
async def des_one(file, key):
    print('即将开始解密', file)
    aes = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)  # IV是偏移量，如果给出就使用，没有就用默认的
    async with aiofiles.open("./movies/电影_源_加密前/{}".format(file), mode='rb') as f1, aiofiles.open(
            "./movies/电影_源_解密后/{}".format(file), mode='rb') as f2:
        # 从加密的文件中读取出来，进行解密，保存到未加密的文件中
        content = await f1.read()
        bs = aes.decrypt(content)  # 解密后是字节
        await f2.write(bs)
    print('文件已经解密', file)


# 解密ts文件
async def des_all_ts_file(key):
    tasks = []
    with open('./movies/m3u8.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            file_name = line.split('/')[-1]  # 获取文件名
            task = asyncio.create_task(des_one(file_name, key))
            tasks.append(task)
    await asyncio.wait(tasks)


# 合并文件
def merge_ts():
    name_list = []
    with open("./movies/m3u8.txt", mode='r', encoding='utf-8') as r:
        for line in r:
            if line.startswith("#"):
                continue
            line = line.strip()
            file_name = line.split('/')[-1]
            name_list.append(file_name)

    # 1、记录当前工作目录
    now_dir = os.getcwd()
    # 2、切换工作目录到需要合并的ts下
    os.chdir("./movies/电影_源_加密前/")
    # 一次合并一部分文件（100个）
    temp = []
    n = 1
    for i in range(len(name_list)):
        name = name_list[i]
        temp.append(name)
        if i != 0 and i % 100 == 0:
            # 合并：mac电脑是： cat a.ts b.ts c.ts > xxx.mp4
            # window电脑是：copy /b a.ts + b.ts + c.ts xxx.mp4
            names = "+".join(temp)
            os.system(r"copy /b {} {}.ts".format(names, n))
            n += 1
            temp = []  # 合并100个还原成初始
        # 把最后没有合并的进行收尾合并
        names = "+".join(temp)
        os.system(r"copy /b {} {}.ts".format(names, n))
    # 把所有的n进行合并
    temp_2 = []
    for i in range(1, n + 1):
        temp_2.append("{}.ts".format(i))
    names = "+".join(temp_2)
    os.system(r"copy /b {} movie.mp4".format(names))
    n += 1
    print(n)
    # 3、所有的操作之后，一定要把工作目录切换回来
    os.chdir(now_dir)


def main():
    url = 'http://www.wbdy.tv/play/30288_2_1.html'

    # 获取视频页的src
    # src_url = get_iframe_src(url)

    # 3、请求到src对应的页面源代码，在该页面中解析出真正的m3u8文件地址
    # m3u8_url = get_first_m3u8_url(src_url)

    # # 下载第二层m3u8文件
    # down_m3u8_file(m3u8_url)

    # # 下载ts文件
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(download_all_ts())
    # loop.close()

    # 合并ts文件
    merge_ts()


if __name__ == '__main__':
    main()
