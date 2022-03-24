import json

import requests

url = r'http://192.168.20.214:10001/Admin/EventFormTypes/CreateEventRecord/'    #网格化事件订单库，新增事件接口
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "SECKEY_CID2=53a070c8e7a456a527ae71bf8c5b833fac755df1; BMAP_SECKEY2=e7ccd76a71cca7384bc9d56993ddbed2e19bbff4744b85e39bb3d65be30e7613e76ae0b8689ae7f5bb14207898aef6950e69432a9314fa542a239fa64bfb5b455c26081c287bdac8c3896b2dfb5dc2e8fac4514bf0987ae4517865731c9f06de1bc2258a4ed3c41de68dc1abd4362550eb2d244caca0a9283dc5cb40bd49cebaa8e4c20ed2ebfdf673a8b956421fb2f8e7c1529c59ef664d6abb46fe3d14c599bad29b69087c06c7f80887368f047512194c06cfe43ee46fdb5e5637d4977854c7e5d0a44e3bdef1b7a658275026eacac8bd593d4bdcc2bc4aa888fd433848e682653e9e39ddf75ee2a4845449ed6e9f; UserName=10000; __RequestVerificationToken=03xez-zOE-_JBMXAgjAbQPR7ybcokaWYg48jz9v13qP1WwnrAP8gY_bxapGID6LK7DWCAirbWS_ygw2IDJgMA-_4wLPWWtQkmPCwCH8P4NA1; ASP.NET_SessionId=s4rynoqfrv1aw0ljx43xqekn; UserId=445d674b-9450-46a5-87fe-98643be068d6"
}
data = {
    '__RequestVerificationToken': 'nDxwnNqtpdHuBclsSxBTYKtdl4yBZLO1w6XaeI-OVfj72ZDhvUwWZwDBn44gEv0jB-mBqWpy6aCr3Sz8xVdfaQ-mJeBMOrd-8lCjPIpPHLg1',
    'Id': '73c16bfa-9043-43b0-a9c0-5cced1efe725',
    'EventFormTypeId': '73c16bfa-9043-43b0-a9c0-5cced1efe725',
    'EnumEventProcType': '1',
    'EnumEventLevel': '0',
    'name': '115',
    'memo': '1',
    'addr': '2',
    'ImgsInJson': '',
    'VideoUrl': '',
    'RecordUrl': '',
    'RecordUrls': '',
    'DepartmentId': 'e22fce3c-c191-4c57-afbe-912c8028d590',
    'PointsInJson': '{"lng":116.933745,"lat":34.737345}'
}
resp = requests.post(url, data=data, headers=header)    #注意data类型
print(resp.text)