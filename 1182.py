N, S = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
combi = []

def bfs(start, depth):
    global ans
    if depth == len(combi):
        if sum(combi) == S:
            ans += 1
        return
    for i in range(start, N):
        combi[depth] = lst[i]
        # print(depth, combi)
        bfs(i+1, depth+1)
# 부분 순열을 다 더한 값을 리턴 , 리스트의 길이가 1, 2, 3, 4,... N까지

for i in range(1, N+1):
    combi = [0] * i
    bfs(0, 0)

print(ans)
    