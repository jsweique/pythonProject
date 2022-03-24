from matplotlib import pyplot
from matplotlib import font_manager

y = [10, 20, 15, 23, 54, 10, 52, 56, 12, 36]
y_1 = [22, 23, 14, 27, 65, 5, 59, 44, 19, 30]
x = [i for i in range(1, 11)]

# 设置中文字体，字体在C:\Windows\Fonts路径下查找
my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STFANGSO.TTF')

# 设置图形大小，需要在创建图之前使用，否则会出现两个图（其中一个空白）
pyplot.figure(figsize=(20, 8), dpi=80)

# label设置图例，color调整折线颜色，linestyle调整线条样式，linewidth调整折线粗细,alpha调整透明度
pyplot.plot(x, y, label='labels图例', color='orange', linestyle='-.', linewidth=5, alpha=0.3)
pyplot.plot(x, y_1, label='y_1得分', color='red')

# 设置x轴刻度，疏密度,rotation调整字体旋转
_xtick_labels = ['2021年{}月'.format(i) for i in x]
pyplot.xticks(x, _xtick_labels, rotation=45, fontproperties=my_font)

_ytick_labels = ['{}次'.format(i) for i in y]
pyplot.yticks(y, _ytick_labels, fontproperties=my_font)

# 绘制网格
pyplot.grid(alpha=0.2)

# 添加图例，解决乱码,跳转图例位置
pyplot.legend(prop=my_font, loc='upper left')

# 添加描述
pyplot.xlabel('月份', fontproperties=my_font)
pyplot.ylabel('次数', fontproperties=my_font)
pyplot.title('测试折线图', fontproperties=my_font)

# 保存图片
# pyplot.savefig('./img/img')
pyplot.show()
