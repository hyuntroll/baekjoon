N, M = map(int, input().split())


combi = [0] * M

def df(start, depth):
    if depth == M:
        print(*combi)
        return
    
    for i in range(start, N):
        combi[depth] = i+1
        df(0, depth+1)

df(0, 0)