import requests
from selenium import webdriver

webdriver_option = webdriver.ChromeOptions()
proxy = 'http://220.175.168.79:9000'

webdriver_option.add_argument('--proxy-server=%s' % proxy)

# web = webdriver.Chrome(options=webdriver_option)
# web.get(r'https://www.baidu.com/')
# web.find_element_by_id('kw').send_keys('ip')
# web.find_element_by_id('su').click()


proxy = {
    "http": "http://118.190.244.234:3128",
    "https": "https://118.190.244.234:3128"
}
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "BIDUPSID=C2E967130A7457AF783BAE40CCB8388C; PSTM=1588125054; BD_UPN=12314753; __yjs_duid=1_166a5baf35c03c29c17b548a221c88ca1619343405971; BDSFRCVID_BFESS=xxtOJeC62CykBg7Hw3O7u0VHVJ6z5sbTH6f3CCWs5AkdLsl-N9b5EG0PeM8g0Ku-S2EqogKKL2OTHmAF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbCe_ILatKI3fP36q4OEh4-bMfQXKKr0aDAX3b7Efbccfq7_bf--D60qQb5z5fvfKDcULCJCWUQUSfb-2-5xy5K_hPntQfoeMj5J2h-5bKQUen6HQT3mXqQbbN3i-4jt-nvJWb3cWh4K8UbShfQPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50eGtet6tDtJks0-5qaJcEHjrlKDTjhPrMjG_jWMT-0bFHXPj_apFbO-3dWqohDhKn34okLfTOLGn7_JjOfIQ2obvpMJ3qjfKR3qjlKMQxtNRy2CnjtpvhKJnee57obUPUXa59LUvL0mcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj0DKLtCvjDb7GbKTD-tFO5eT22-usaDcT2hcHMPoosIJuytnjybbyXNOtJp57QDQLoqIhtMbUoqRHQJ6UW-_n3NOv-U7pWDTm_q5TtUJMqDThbn3TqfLn5MOyKMniBnr9-pnE0lQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDj-WDjJ0DGRKaC6aKC5bL6rJabC3J-nmXU6qLT5XLprW3t-fWTke2K3atUQ1SlFC26o5-l0njxDe3MJU-bTCBbb1-b4V8CTPjfonDh88XH7MJUntHGAHK4jO5hvv8KoO3M7VLfKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRPOoC0-3q; BDUSS=WhMYTBMcX5BR1l-VThHRUFMM25jUnh1UjZmejlQeTQySWhQekFDRDkxSUo2TnRoRVFBQUFBJCQAAAAAAAAAAAEAAACo3VqDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlbtGEJW7RhV; BDUSS_BFESS=WhMYTBMcX5BR1l-VThHRUFMM25jUnh1UjZmejlQeTQySWhQekFDRDkxSUo2TnRoRVFBQUFBJCQAAAAAAAAAAAEAAACo3VqDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlbtGEJW7RhV; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-316%3A; BAIDUID_BFESS=F918AA791105DD549C957A6EC23BAB2D:FG=1; baikeVisitId=c8d33eaa-aed6-44aa-8c26-ca5bcd7c16de; channel=baidusearch; COOKIE_SESSION=22092_0_9_9_11_4_1_0_9_3_21_1_5936_0_0_0_1639389790_0_1639389783%7C9%2324511_745_1637653849%7C9; BD_HOME=1; delPer=0; BD_CK_SAM=1; PSINO=6; H_PS_PSSID=35104_35239_35435_34584_35348_35246_34873_35329_35321_26350_35478_22160; BDSVRTM=27; WWW_ST=1639457033616",
    "Host": "www.baidu.com",
    "is_referer": "https://www.baidu.com/",
    "is_xhr": "1",
    "Pragma": "no-cache",
    "Referer": "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip&fenlei=256&rsv_pq=9c0431da0026e41b&rsv_t=4456kMnxuiejqQ22m3E0ZVCNJN8uzi7nS1wIkRXKPEEejyExtxIAY4tnbpA&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_sug3=4&rsv_sug1=3&rsv_sug7=101&rsv_btype=i&inputT=7205&rsv_sug4=8475",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}
resp = requests.get(r'http://www.baidu.com', headers=head,proxies=proxy)
# resp = requests.get(
#     r'http://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=F918AABAB2D45872&ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip&fenlei=256&rsv_pq=9c0431da0026e41b&rsv_t=4456kMnxuiejqQ22m3E0ZVCNJN8uzi7nS1wIkRXKPEEejyExtxIAY4tnbpA&rqlang=cn&rsv_dl=tb&rsv_enter=0&rsv_sug3=4&rsv_sug1=3&rsv_sug7=101&rsv_btype=i&inputT=7205&rsv_sug4=8475&rsv_sid=35104_35239_35435_34584_35348_35246_34873_35329_35321_26350_22160&_ss=1&clist=&hsug=&f4s=1&csor=2&_cr1=32653',
#     headers=header, proxies=proxy)
resp.encoding = 'utf-8'
r = resp.status_code
print(r)
