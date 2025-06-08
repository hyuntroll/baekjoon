n = int(input())

cnt = 1
dancing = {"ChongChong": True}
for _ in range(n):
    a, b = input().split()
    if a not in dancing:
        dancing[a] = False
    if b not in dancing:
        dancing[b] = False

    if dancing[a] and not dancing[b]:
        dancing[b] = True
        cnt += 1
    elif dancing[b] and not dancing[a]:
        dancing[a] = True
        cnt += 1

print(cnt)