import json

import requests

url = r'http://192.168.20.214:10001/Login/Login'
data = {
    'loginName': '10000',
    'sk': 'b294792b7bb93344fef8b31cc3e7abb5',
    'ValidateCode': '2618',
    '__RequestVerificationToken': 'whtamXZBoR1Duf5RRVqwm1Yv1c_I7lFB3BVArujkrja0xcFvdPo5kB-qNkR9eCNaS7KngBQpJNE9qT8e49LxYUWKM0GDwcrPxqXIP2vCS3A1'
}

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
resp = requests.post(url, data=json.dumps(data), headers=header)
print(resp.text)
print(resp.headers)
