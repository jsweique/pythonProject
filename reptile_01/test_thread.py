from concurrent.futures import ThreadPoolExecutor
from threading import Thread


def func(name):
    for i in range(100):
        print(name, i)


def fn(res):
    print(res.result())  # 获取返回值,上一个函数要有返回值


# t1 = Thread(target=func, args=("周杰伦",))
# t2 = Thread(target=func, args=("王力宏",))
# t3 = Thread(target=func, args=("周润发",))
# t1.start()
# t2.start()
# t3.start()

# with ThreadPoolExecutor(10) as t:  # 创建线程池
#     t.submit(func, "周杰伦")
#     t.submit(func, "王力宏")
#     t.submit(func, "王富贵")

with ThreadPoolExecutor(3) as t:
    t.submit(func, "周杰伦").add_done_callback(fn)  # 返回即执行callback函数

    result = t.map(func, ["周杰伦", "王力宏", "王富贵"])
    # map返回值是生成器，返回值的内容和任务分发顺序是一致的



'''
何时使用多线程，何时使用多进程：
1、多线程：任务相对同意，弧线特别相似
2、多进程：多个任务互相独立，很少有交集

获取免费IP池：
    1、从各个免费网站上抓取代理IP
    2、验证代理IP是否可用
    3、主办对外的接口
'''