import math

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2 )
    d2 = max(r1, r2) - min(r1, r2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif d2 < d < r1 + r2:
        print(2)
    elif r1 + r2 == d or d2 == d:
        print(1)
    elif r1 + r2 < d or d < d2:
        print(0)
    