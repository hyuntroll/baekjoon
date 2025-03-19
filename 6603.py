while True:
    N, *lst = map(int, input().split())
    if N == 0:
        break
    # lst = [ 1, 2, 3 ,4, 5, 6, 7 ]
    combi= [0] * 6

    def bfs(start, depth):
        if depth == 6:
            print(*combi)
            return

        for i in range(start, N):
            combi[depth] = lst[i]
            # print(*combi, depth)
            bfs(i+1, depth+1)

    bfs(0, 0)
    print()