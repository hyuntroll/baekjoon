import sys; input = sys.stdin.readline
from collections import Counter

n = int(input())

lst = sorted([int(input()) for i in range(n)])
print(round(sum(lst)/n))
print(lst[(len(lst)+1)//2 -1])
counter = Counter(lst)
dit = {}
for i in lst:
    if i in dit:
        dit[i] += 1
    else:
        dit[i] = 0
m = max(dit.values())
mm = [i for i in dit if dit[i] == m]
print(mm[0] if len(mm) == 1 else mm[1])

print(max(lst) - min(lst))
### 5 