import re

import requests

url = r'http://192.168.20.214:10001/EventRecords/IndexList'
parm = {
    'pageSize': '20',
    'offset': '0',
    'sortOrder': 'asc',
    'keyword': '',
    'DepartmentId': '',
    'DepartmentFullPath': '',
    'EventFormTypeId': '',
    'EnumOrderStatus': '',
    'EnumEventLevel': '',
    'EnumEventProcType': '',
    'EnumDataSource': '',
    'DTT': '2021-11-12',
    'DTF': '2021-10-11',
    '_': '1636597750492'
}
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Cookie": "UserName=10000; __RequestVerificationToken=03xez-zOE-_JBMXAgjAbQPR7ybcokaWYg48jz9v13qP1WwnrAP8gY_bxapGID6LK7DWCAirbWS_ygw2IDJgMA-_4wLPWWtQkmPCwCH8P4NA1; ASP.NET_SessionId=s4rynoqfrv1aw0ljx43xqekn; UserId=445d674b-9450-46a5-87fe-98643be068d6"
}

# 配置代理
proxy = {
    "http": "http://113.237.3.178:9999",
    "https": "https://113.237.3.178:9999"
}
# 请求中接入代理
resp=requests.get(url,proxies=proxy)

resp = requests.get(url, params=parm, headers=header)
print(resp.text)
r = resp.text  # 使用text,json()的话，后面无法截取
# resp.encoding()


obj = re.compile(r'"Code":"(?P<code>.*?)","Title":"(?P<name>.*?)","Content":"',
                 re.S)  # 获取返回值中的事件编号、事件标题，re.S 过滤换行（.没有过滤换行符）
result = obj.finditer(r)
# obj.search(r).group('code')
# obj.search(r).group('title')
for item in result:
    print(item.group('code'))
    print(item.group('name'))
