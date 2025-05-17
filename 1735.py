def gcd(a, b):
    while True:
        r = a%b
        if r == 0:
            break
        a = b
        b = r
    return b

a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = a*d + b*c, b*d
print(e//gcd(e, f), f//gcd(e, f), sep=" ")


