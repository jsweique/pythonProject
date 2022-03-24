from pyquery import PyQuery

html = """
    <ul>
        <li class="aaa"><a href="http://www.google.com">谷歌</a></li>
        <li class="aaa" id="xx"><a href="http://www.baidu.com">百度</a></li>
        <li class="bbb"><a href="http://www.qq.com">腾讯</a></li>
        <li class="ccc"><a href="http://www.yuanlai.com">猿来</a></li>
    </ul>
"""

p = PyQuery(html)
c = p('li')('a').text()  # 拿文本
print(c)

a = p('.aaa')  # class="aaa"
print(a)
b = p('.ccc a').attr("href")  # 根据class拿属性
print(b)

d = p("#xx a").text()  # 根据id拿内容
print(d)

it = p("li a").items()  # 获取多个a标签
for item in it:
    href = item.attr("href")
    text = item.text()
    print(text, href)

html2 = """
<HTML>
    <div class='aaa'>111</div>
    <div class='bbb'>222</div>
<HTML>
"""
# 在某个标签后面添加新标签
p1 = PyQuery(html2)
p1("div.aaa").after("""<div class='ccc'>333</div>""")  # 在标签后面添加标签
p1("div.aaa").append("""<span>444</span>""")  # 在标签的里面添加标签
p1("div.bbb").attr("class", "aaa")  # 修改标签class属性bbb为aaa
p1("div.aaa").attr("id", "123456")  # 给标签添加属性
p1("div.aaa").remove_attr("id")  # 删除id属性
p1("div.bbb").remove()  # 删除标签
text = p1('div')
print(text)
