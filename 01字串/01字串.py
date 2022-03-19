# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""
for i in range(0, 31):
    s = str(bin(i))[2:]
    if len(s)<5:
        s = (5-len(s))*"0"+s
    print(s)
