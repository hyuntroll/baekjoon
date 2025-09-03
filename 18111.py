N, M, b = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
mx = 0; mn = False
for l in lst:
    mx = max(mx, max(l))
    if mn == False:
        mn = min(l)
    else:
        mn = min(mn,min(l))

ans = 0
t = 0
# 다 부숴보던가
for i in range(N):
    for k in range(M):
        t += (lst[i][k] -mn) * 2
        b += lst[i][k] -mn
print(t, mn)


# 설치하고 부숴서 해보던가


