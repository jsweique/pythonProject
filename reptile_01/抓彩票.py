import requests
from bs4 import BeautifulSoup

url = r'https://kaijiang.78500.cn/ssq/'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}
resp = requests.get(url, headers=header)
print(resp.text)
con = BeautifulSoup(resp.text, "html.parser")
tbody = con.find('tbody',attrs={'class': 'list-tr'})
tr = tbody.find_all('tr')
for t in tr:
    td1 = t.find_all('td')[0].text.strip()
    td2 = t.find_all('td')[1].text.strip()
    tasks=[]
    tds3=t.find_all('span')
    for td3 in tds3:
        tasks.append(td3.text.strip())
    tds3=','.join(tasks)
    td4 = t.find_all('td')[3].text.strip()
    td5 = t.find_all('td')[4].text.strip()
    td6 = t.find_all('td')[5].text.strip()
    td7 = t.find_all('td')[6].text.strip()
    td8 = t.find_all('td')[7].text.strip()
    td9 = t.find_all('td')[8].text.strip()
    td10 = t.find_all('td')[9].text.strip()
    td11 = t.find_all('td')[10].text.strip()
    with open(r'C:\Users\zheng\PycharmProjects\pythonProject\reptile_01\img\ssq.csv', mode='a',
              encoding='utf-8') as w:
        # n=td1.text.strip()
        w.write(td1+','+td2+','+tds3+','+td4+','+td5+','+td6+','+td7+','+td8+','+td9+','+td10+','+td11)
        # w.write(',')
        w.write('\n')
    # with open(r'C:\Users\zheng\PycharmProjects\pythonProject\reptile_01\img\ssq.csv', mode='a',
    #           encoding='utf-8') as w: