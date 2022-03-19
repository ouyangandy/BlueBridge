# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""
# y = int(input())
# if y%4 == 0 and y%100 !=0 or y%400==0:
#     print('yes')
# else:
#     print("no")
#
#
# # 圆的面积
# import math
# r = float(input())
# area = math.pi*r*r
# print("%.7f"%(area))
#
#
# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)
#
# from functools import reduce
# n = int(input())
# print(reduce(lambda x, y: x + y, range(1, n+1)))

n = int(input())
l = list(range(n+1))
print(sum(l))
