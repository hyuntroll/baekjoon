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



for i in range(int(input())):
    print(lcm(*list(map(int, input().split()))))