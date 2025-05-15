N, M = map(int, input().split())

a = {input(): 1 for _ in range(N)}
b = [input() for _ in range(M)]

print(a)
cnt = 0
for i in b:
    if a.get(i):
        cnt += 1
print(cnt)
