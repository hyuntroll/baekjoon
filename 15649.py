N, M = map(int, input().split())

combi = [0] * M
visited = [False] * N

def bf(start, depth):
    if depth == M:
        print(*combi)
        return

    for i in range(start, N):
        if visited[i] == False:
            combi[depth] = i+1
            visited[i] = True

            # print("아야", *visited)

            bf(0, depth+1)
            visited[i] = False

bf(0, 0)
