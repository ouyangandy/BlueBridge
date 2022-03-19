# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""

n = int(input())
def generate(numRows):
    if numRows == 0:
        return []
    l1 = [[1]]
    n = 1
    while n < numRows:
        l1.append(list(map(lambda x, y: x + y, [0] + l1[-1], l1[-1] + [0])))
        n += 1
    return l1
li = generate(n)
for i in li:
    j = 0
    while j<len(i):
        print(i[j], end=' ')
        j+=1
    print(end="\n")