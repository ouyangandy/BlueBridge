class Solution:
    def roteteString(self, s, offset):
        print(s)
        if len(s) > 0:
            offset = offset % len(s)
            print(offset,len(s))
        temp = (s + s)[len(s) - offset: 2 * len(s) - offset]
        for i in range(len(temp)):
            s[i] = temp[i]


if __name__ == "__main__":
    s = ['a', 'b']
    offset = 3
    solution = Solution()
    solution.roteteString(s, offset)
    # print('输入：s = ', ['a', 'b', 'c', 'd', 'e', 'f', 'g'], ' ', 'offset=', offset)
    print('输出：s = ', s)

