from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id='10086'>周大枪</nick>
        <nick id='10010'>周芷若</nick>
        <nick class='jay'>周杰伦</nick>
        <nick class='jolin'>蔡依林</nick>
        <div>
            <nick>这</nick>
        </div>
    </author>
    <partner>
        <nick id='ppc'>胖胖陈</nick>
        <nick id='ppbc'>胖胖不陈</nick>
    </partner>
</book>
"""

# 如果pcharm报错，可以考虑这种导入方式
# from lxml import html
# etree=html.etree


et = etree.XML(xml)
result = et.xpath('/book')  # /表示根节点
result = et.xpath('/book/name')  # 在xpath中间的/表示的是儿子
result = et.xpath('/book/name/text()')[0]  # text() 拿文本
result = et.xpath('/book//nick')  # //表示的是子孙后代
result = et.xpath('/book/*/nick/text()')  # *通配符 （谁都行）
result = et.xpath('/book/author/nick[@id="10086"]/text()')  # []表示属性筛选 @属性名=值  find（nick,attrs={'class':'jay'})
result = et.xpath('/book/author/nick[@class="jay"]/text()')
result = et.xpath('/book/partner/nick/@id')  # 最后一个/表示拿到nick里面的id的内容，@属性，可以直接拿到属性值
print(result)
