n, m = map(int, input().split())
dit = {}
for i in range(n+m):
    n = input()
    if n not in dit:
        dit[n] = 0
    else:
        dit[n] += 1
print(sum([1 for k in dit if dit[k] == 1]))
for k in sorted(dit):
    if dit[k] == 1:
        print(k)
