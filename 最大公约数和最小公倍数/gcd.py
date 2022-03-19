# 最大公约数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 最小公倍数
def gcm(c, d):
    return c * d / gcd(c, d)


