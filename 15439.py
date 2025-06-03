# N 받았을 때 nP2 하면 될거같은뎀 n일땐 성립 안되니까 0 5P2
n = int(input())
if n < 2:
    print(0)
else:
    rs = 1
    for i in range(n, n-2, -1):
        rs *= i
    print(rs)