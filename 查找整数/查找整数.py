# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""
n=int(input())
b=list(map(int,input().split()))
c=int(input())
k=1
for i in b:
    if c==i:
        print(k)
        break
    k=k+1
else:
    print(-1)

