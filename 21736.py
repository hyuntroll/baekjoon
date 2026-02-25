import queue
row, col = map(int, input().split())
lst = []
y, x = 0, 0
for i in range(row):
    lst.append(list(input()))

    for j in range(col):
        if lst[i][j] == "I":
            y, x = i, j

dist_x = (1, 0, -1, 0)
dist_y = (0, 1, 0, -1)

def dfs(cur_pos):
    q = queue.Queue()
    q.put(cur_pos)
    count = 0

    while not q.empty():
        y, x = q.get()
        for i in range(4):
            dy = y + dist_y[i]
            dx = x + dist_x[i]
            if 0 <= dy < row and 0 <= dx < col:
                if lst[dy][dx] == "O" or lst[dy][dx] == "P":
                    q.put((dy, dx))
                    if lst[dy][dx] == "P":
                        count += 1
                    lst[dy][dx] = "Z"
    return count if count != 0 else "TT"

print(dfs((y, x)))