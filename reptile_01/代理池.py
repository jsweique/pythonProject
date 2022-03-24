import random
import time

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# 获取ip地址
class TestProxy:
    def __init__(self):
        pass

    def get_user_agent(self):
        self.user_agents = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
        ]
        self.user_agent = random.choice(self.user_agents)
        return self.user_agent

    def get_ip(self, url):
        header = {
            "User-Agent": self.get_user_agent()
        }
        resp = requests.get(url, headers=header)
        try:
            resp2 = BeautifulSoup(resp.text, 'html.parser')
            tbody = resp2.find('tbody')
            tr = tbody.find_all('tr')
            for t in tr:
                td = t.find_all('td')
                for tt in td:
                    ip = tt.text.strip()
                    print(ip)
                    with open(r'C:\Users\zheng\PycharmProjects\pythonProject\reptile_01\img\ip2.csv', mode='a',
                              encoding='utf-8') as w:
                        w.write(ip + ',')
                with open(r'C:\Users\zheng\PycharmProjects\pythonProject\reptile_01\img\ip2.csv', mode='a',
                          encoding='utf-8') as w:
                    w.write('\n')
            print('数据下载完毕,地址：{}'.format(url))
            time.sleep(3)
        except:
            print('!!!打开地址异常,地址：{}'.format(url))


# 验证代理IP是否可用
class VerificationProxy:
    def __init__(self):
        pass

    def verification_proxy(self):
        df = pd.read_csv(r'C:\Users\zheng\PycharmProjects\pythonProject\reptile_01\img\ip.csv', header=None,
                         names=["ip", "port", "transparent", "agreement", "adress", "time", "date", "none"])
        # proxy_types = ["{}".format(i) for i in np.array(df['proxy_type'])]
        ips = ["{}".format(i) for i in np.array(df['ip'])]
        ports = ["{}".format(i) for i in np.array(df['port'])]

        proxy_url = ['{}:{}'.format(ips[i], ports[i]) for i in range(len(ips))]
        # proxy_urls = ['https://{}:{}'.format(ips[i], ports[i]) for i in range(len(ips))]

        proxy_type = ['http', 'https']
        for i in range(len(ips)):
            time.sleep(1)
            proxies = {
                proxy_type[0]: proxy_type[0] + r'://' + proxy_url[i],
                proxy_type[1]: proxy_type[1] + r'://' + proxy_url[i]
            }
            try:
                response = requests.get(r'http://www.baidu.com', proxies=proxies)
            except Exception as e:
                print('invalid ip and port......:' + proxy_url[i])
            else:
                code = response.status_code
                if code == 200:
                    print('effective ip:' + proxy_url[i])
                    with open(r'C:\Users\zheng\PycharmProjects\pythonProject\reptile_01\img\effective_ip.csv', 'a+',
                              encoding='utf-8-sig') as f:
                        f.write(proxy_url[i] + '\n')
                else:
                    print('invalid ip and port:' + proxy_url[i])


# 返回验证后的IP
class GetProxies:
    def __init__(self):
        pass

    def get_proxies(self):
        df = pd.read_csv(r'C:\Users\zheng\PycharmProjects\pythonProject\reptile_01\img\effective_ip.csv', header=None,
                         names=['ip'])
        ips = []
        for ip in np.array(df['ip']):
            ips.append(ip)
        return ips


# 获取IP举例
def test():
    ips = GetProxies().get_proxies()
    proies = {
        "http": ips[random.randint(0, len(ips))]
    }
    response = requests.get(r'https://www.baidu.com/', proxies=proies)
    response.encoding = 'utf-8'
    print(response.text)


# VerificationProxy().verification_proxy()

for i in range(1, 4378):
    url = r'https://www.kuaidaili.com/free/intr/{}/'.format(i)
    TestProxy().get_ip(url)
    time.sleep(2)
