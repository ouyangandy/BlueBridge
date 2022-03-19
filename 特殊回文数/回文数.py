# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""
# 第三方库，不能使用，
from pythonds.basic.deque import Deque


def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    if stillEqual == True:
        return 'yes!'
    else:
        return 'no!'
print(palchecker(input()))