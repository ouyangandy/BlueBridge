# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/11 16:12
@Author  : andy
"""

from collections import deque
charDeque = deque()
string = input()
stillEqual = True
for i in range(len(string)):
    charDeque.append(i)
while len(charDeque) > 1 and stillEqual:
    first = charDeque.pop()
    last = charDeque.popleft()
    if first or last in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        stillEqual = False
    if first != last:
        stillEqual = False
if not stillEqual:
    print('yes!')
else:
    print('no!')


from collections import deque
charDeque = deque()
string = input()

def huiwen(s):
    for i in s:
        charDeque.append(i)
    while len(charDeque) > 1:
        last = charDeque.pop()
        first = charDeque.popleft()
        if first != last:
            return 'no!'
    return 'yes!'
print(huiwen(string))