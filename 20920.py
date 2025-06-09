import sys; input=sys.stdin.readline
n, m = map(int, input().split())
dit = {}
for _ in range(n):
    na = input().rstrip()
    if len(na) >= m:
        if na not in dit:
            dit[na] = 1
        else:
            dit[na] += 1

# 소트를 먼저 해두는 이유는 파이썬 내장 정렬은 안정 정렬이기 때문
# 
sorted_lst = sorted(sorted(dit.keys()), reverse=True, key=lambda x: (dit[x], len(x)))
print(*sorted_lst, sep="\n")