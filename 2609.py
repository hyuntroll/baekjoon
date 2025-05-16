def gcd(a, b):
    while True:
        r = a%b
        if r == 0:
            break
        a = b
        b = r
    return b

def lcm(a, b):
    return (a * b ) // gcd(a, b)

a, b = map(int, input().split())

print(gcd())
print(lcm())