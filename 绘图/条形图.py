from matplotlib import pyplot
from matplotlib import font_manager

'''
绘制2017年内地电影票房前20的电影(列表a)和电影票房数据(列表b),那么如何更加直观的展示该数据?
'''
a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5∶\n最后的骑士", "摔跤吧!爸爸", "加勒比海盗5:\n死无对证", "金刚:骷髅岛", "极限特工︰\n终极回归",
     "生化危机6:\n终章", "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3\n∶殊死一战", "蜘蛛侠\n:英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊"]
b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
     6.86, 6.58, 6.23]

my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STFANGSO.TTF')

pyplot.figure(figsize=(20, 8), dpi=80)
pyplot.bar(a, b, width=0.3)
# pyplot.bar(range(len(a)), b,width=0.3)
# pyplot.xticks(range(len(a)), a)
pyplot.xticks(a, a, fontproperties=my_font, rotation=45)
pyplot.show()
