import queue
# 숫자, 간선
n, m = map(int, input().split())

node = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    node[a][b] = node[b][a] = 1

def st(start , length):
    INF = float('inf')
    distances = [INF] * (length + 1)
    distances[start] = 0
    q = queue.Queue()
    q.put((0, start))

    while not q.empty():
        current_dist, current_v = q.get()

        if current_dist > distances[current_v]:
            continue

        for i in range(1, length + 1):
            if node[current_v][i] != 0:
                distance = current_dist + 1
                if distance < distances[i]:
                    distances[i] = distance
                    q.put((distance, i))

    return sum(distances[1:])

min_ = st(1, n)
min_i = 1
for i in range(2, n+1):
    az = st(i, n)
    if az < min_:
        min_ = az
        min_i = i
print(min_i)