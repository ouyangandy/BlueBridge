while True:
    try:
        n = int(input())
        s = []
        for i in range(n):
            s.append(input().split())
        for i in range(0,n):
            flag = 0
            for j in range(n):
                if s[j][i] == '1':
                    flag += 1
            if flag >= n/2:
                print(i+1,'',end='')
    except:
        break
