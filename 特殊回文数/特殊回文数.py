# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""
n = int(input())
for i in range(10000,999999):
    if str(i) == str(i)[::-1]:
        sum  = 0
        for j in str(i):
            sum+=int(j)
        if sum == n:
            print(i)
