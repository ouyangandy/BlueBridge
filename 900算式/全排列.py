# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""



import itertools #python的迭代器模块
# 全排列
b = [1,2,3] #迭代类型可以是列表，元组，字符串等
d = itertools.permutations(b,3) # 第一个参数代表迭代的序列，第二个代表参与排列的元素个数
for i in d:
    print(i)


print('###########################')

# 笛卡尔积
b = [1,2,3]
k = [4,5]
c = itertools.product(b,k,repeat=1)
for i in c:
    print(i)

# 全组合
b = [1,2,3]
e = itertools.combinations(b,2)
for i in e:
    print(i)

