# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""
def main():
    n=int(input())
    lst1=input().strip().split(' ')
    lst2=[]
    for i in lst1:
        lst2.append(int(i))
    lst2.sort()
    Sum=0
    for j in lst2:
        Sum=Sum+j
    print(str(lst2[len(lst2)-1]))
    print(str(lst2[0]))
    print(str(Sum))
main()