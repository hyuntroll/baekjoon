N = int(input())
lst = list(map(int, input().split()))

ans = 0

for i in lst:
    if len([k for k in range(1, i+1) if i % k == 0]) == 2:
        ans += 1

print(ans)