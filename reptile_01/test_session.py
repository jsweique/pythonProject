import requests

url1 = 'http://192.168.20.214:10003/Login/Login'
data = {
    'loginName': '10000',
    'loginPsd': '111111'
}
se = requests.session()
resp = se.post(url1, data=data)
print(resp.text)
print(resp.cookies)

url2 = 'http://192.168.20.214:10003/PMServices/IndexList?pageSize=20&offset=0&sortOrder=asc&keyword=&_=1637041282604'
resp02 = se.get(url2)
print(resp02.json())
lis = resp02.json()['rows']
print(lis)
print(lis[0]['Name'])
