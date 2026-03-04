from queue import Queue
n, m, v = map(int, input().split())
arr = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

def DFS(arr, s, visited):
    visited[s] = True
    print(s+1, end=' ')
    for v in range(n):
        if arr[s][v] != 0 and not visited[v]:
            DFS(arr, v, visited)

def BFS(arr, s, visited):
    visited[s] = True
    que = Queue()
    que.put(s)
    while not que.empty():
        v = que.get()
        print(v+1, end=' ')
        for i in range(n):
            if arr[v][i] != 0 and not visited[i]:
                que.put(i)
                visited[i] = True

DFS(arr, v-1,[False] * n)
print()
BFS(arr, v-1, [False] * n)