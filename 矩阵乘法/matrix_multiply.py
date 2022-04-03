# -*- coding: utf-8 -*-

"""
@Time    : 2022/4/3 21:28
@Author  : andy
"""

def fun(a, b):
    global n, m, k
    c = [[0 for i in range(k)] for i in range(n)]
    for i in range(n):
        for j in range(k):
            for k1 in range(m):
                c[i][j] += a[i][k1] * b[k1][j]
    return c


if __name__ == '__main__':
    n, m, k = list(map(int, input().strip().split(" ")))
    a = []
    b = []
    for i in range(n):
        temp = list(map(int, input().strip().split(" ")))
        a.append(temp)
    for i in range(m):
        temp = list(map(int, input().strip().split(" ")))
        b.append(temp)

    # print(a,b)
    res = fun(a, b)
    # print(res)
    for i in range(n):
        for j in range(k):
            print(res[i][j], end=' ')
        print()




