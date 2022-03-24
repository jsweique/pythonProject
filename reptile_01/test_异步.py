import asyncio

import aiofiles
import aiohttp


async def download(url):
    print('开始下载', url)
    file_name = url.split('/')[-1]
    async with aiohttp.ClientSession() as session:  # 相当于requests
        async with session.get(url) as resp:
            content = await resp.content.read()
            async with aiofiles.open('./img/' + file_name, mode='wb') as f:
                await f.write(content)
    print('下载完成', url)


async def main():
    url_list = [
        "http://pic3.hn01.cn/wwl/upload/2021/09-06/ukjvgnda0v4.jpg",
        "http://pic3.hn01.cn/wwl/upload/2021/09-06/b5jd5unjn3a.jpg",
        "http://pic3.hn01.cn/wwl/upload/2021/09-06/g3052rhpuwf.jpg",
        "http://pic3.hn01.cn/wwl/upload/2021/09-06/zkvwrjvazfa.jpg",
    ]
    tasks = []
    for url in url_list:
        t = asyncio.create_task(download(url))
        tasks.append(t)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
