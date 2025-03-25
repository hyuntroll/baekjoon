import math
N = int(input())
M = int(input())

ans = 0
min_n = math.inf

for i in range(N, M+1):
    if len([k for k in range(1, i+1) if i % k == 0]) == 2:
        ans += i
        min_n = min(min_n, i)

if ans != 0:
    print(ans)
    print(min_n)
else:
    print(-1)



###########