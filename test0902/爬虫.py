import requests

# r = requests.get('http://www.baidu.com')
# print(r.content.decode('utf-8'))

#百度网页保存到本地
with open('baidu','w') as write:
    write.write(requests.get('http://www.baidu.com').content.decode('utf-8'))
