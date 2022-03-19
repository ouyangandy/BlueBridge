# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""
# 10进制转16进制: hex(16)  ==>  0x10
# 16进制转10进制: int('0x10', 16)  ==>  16
# 类似的还有oct()， bin()
# 16-10-8

def main1():
    n = int(input())
    lst = []
    for i in range(n):
        num1 = input()
        lst.append(num1)
    for num2 in lst:
        print('{:o}'.format(int(('0x' + num2), 16)))

# 16-10
def main2():
    s = input()
    print('{}'.format(int(('0x' + s), 16)))

def main3():
    a = int(input())
    n = str(hex(a))[2:]
    print(n.upper())
main3()

