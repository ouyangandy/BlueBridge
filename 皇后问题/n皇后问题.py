# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""

# https://blog.csdn.net/qq_43235359/article/details/90605468
def check(board, row, col):
    for i in range(row):
        if abs(board[i] - col) == 0 or abs(board[i] - col) == abs(i - row):
            return False
    return True

count = 0
def eightqueen(board, row):
    border = len(board)
    if row >= border:
        global count
        count += 1
        for i, col in enumerate(board):
            print('□  ' * col + '■  ' + '□  ' * (len(board) - 1 - col))
        print("")

    for col in range(border):
        if check(board, row, col):
            board[row] = col
            eightqueen(board, row + 1)

board = [0 for i in range(4)]
eightqueen(board, 0)
print(count)


# 第二种：https://www.cnblogs.com/ChangAn223/p/10940455.html
'''
# 检测（x,y）这个位置是否合法（不会被其他皇后攻击到）
def is_attack(queue, x, y):
    for i in range(x):
        if queue[i] == y or abs(x - i) == abs(queue[i] - y):
            return True
    return False


# 按列来摆放皇后
def put_position(n, queue, col):
    for i in range(n):
        if not is_attack(queue, col, i):
            queue[col] = i
            if col == n - 1:    # 此时最后一个皇后摆放好了，打印结果。
                print(queue)
            else:
                put_position(n, queue, col + 1)


n = 4       # 这里是n 就是n皇后
queue = [None for i in range(n)]        # 存储皇后位置的一维数组，数组下标表示皇后所在的列，下标对应的值为皇后所在的行。
put_position(n, queue, 0)
'''






