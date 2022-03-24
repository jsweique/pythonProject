from bs4 import BeautifulSoup

html = """
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
"""
resp = BeautifulSoup(html, "html.parser")
r = resp.find_all('a')
for r1 in r:
    r2 = r1.text  # 获取标签的内容
    r3 = r1.get('href')  # 获取标签的属性值
    r4 = r1.get('class')
    print(r2, r3, r4)

print('------------')
results = resp.find('p')
print(results.text)

print('--------------------')
result02=resp.find_all('a')
print(result02[1].text)
