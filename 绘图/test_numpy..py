import numpy as np

a = np.arange(1, 7)

b = a.reshape(2, 3)  # 不改变原数组维度
# a.shape = (2, 3)  # 改变原数组的维度，2行3列
print(a, id(a))
print(b, id(b))
a.astype(float)
print(a > 3)  # 比较数组中每个元素的值，返回False True数组
print(a + a)  # 两个数组中的值分别相加
print(a * 4)  # 数组中每个元素都乘以4

