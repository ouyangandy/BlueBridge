# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/3 21:36
@Author  : andy
"""
mn = input().split()
N = int(mn[0])
M = int(mn[1])

# 导入矩阵
rect = []
for x in range(0, N):
    apend_rect = input().split()
    rect.append(apend_rect)
# 创造一个储存最终结果的矩阵rect_new
rect_new = [[0 for _ in range(0, N)] for _ in range(0, N)]
# 创造一个中间过度作为输入的矩阵rect)mid
rect_mid = rect
# 判断是否进行0次幂计算，如果是的话输出一个对角矩阵
if M == 0:
    for i in range(0, N):
        rect_new[i][i] = 1
        result = ""
        for j in range(0, N):
            result += " " + str(rect_new[i][j])
        print(result[1:])
else:
    # 如果只进行一次计算的话，输出它本身
    if M == 1:
        rect_new = rect
    else:
        for i in range(0, M - 1):
            # 这里要注意每次要将rect_new清零不然会累加
            rect_new = [[0 for _ in range(0, N)] for _ in range(0, N)]
            a = 0
            # a为行计算，b为列计算，用while就可以先把一行的所有的数计算出来
            while a < N:
                b = 0
                while b < N:
                    for j in range(0, N):
                        rect_new[a][b] += int(rect_mid[a][j]) * int(rect[j][b])
                    b += 1
                a += 1
            # 将计算的后的矩阵赋值给中间矩阵作为下一次的输入
            rect_mid = rect_new
    # 输出
    for i in range(0, N):
        result = ""
        for j in range(0, N):
            result += " " + str(rect_new[i][j])
        print(result[1:])

