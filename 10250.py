n = int(input())

for i in range(n):
    h, w, c = map(int, input().split())
    y = c%h
    x = c//h +1
    if y == 0:
        y = h
        x -= 1
    print(f"{y}{x:02}")


# 이건 나중에 다시