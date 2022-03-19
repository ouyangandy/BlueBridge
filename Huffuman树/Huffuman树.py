# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""
n = int(input())
li = list(map(int, input().split(" ")))
sum = 0
while len(li) > 1:
    min1 = min(li)
    li.remove(min1)
    min2 = min(li)
    li.remove(min2)
    li.append(min1+min2)
    sum = sum + min1+min2
print(sum)
