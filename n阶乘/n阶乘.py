# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""
# 不能使用递归
def run():
    n = int(input())
    out = 1
    for i in range(1, n+1):
        out *= i
    print(out)
run()

a = int(input())
b = int(input())
print(a+b)
