# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""
# a-z：97-122
# A-Z：65-90

# ch=input("请输入一个字符：")
# print(ch,"的ASCII码为：",ord(ch))
#
# ch=input("请输入对应的ASCII码：")
# ch=int(ch)                       #以字符串的形式接收键盘输入的内容，所以要对其进行转换
# print(ch,"的ASCII码为：",chr(ch))

n, m = list(map(int, input().split()))
for r in range(1, n + 1):  # 进行n次循环，每次循环输出一行
    for l in range(1, m + 1):  # 进行m次循环，输出m个字母
        if r - l > 0:
            print(chr(65 + r - l), end='')
        else:
            print(chr(65 - r + l), end='')
    print('')
