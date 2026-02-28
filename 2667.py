import sys
import queue
input = sys.stdin.readline
dist_row = (-1, 0, 1, 0)
dist_col = (0, 1, 0, -1)

n = int(input())
lst = []
count = 0

for i in range(n):
    temp = input()
    for j in range(n):
        if temp[j] == "1":
            lst.append((i, j))
            count += 1
visited = [False] * count

counts = {}
c = 0
for i in range(count):
    if not visited[i]:
        c += 1
        counts[c] = 0

        q = queue.Queue()
        q.put(i)
        visited[i] = True
        while not q.empty():
            counts[c] += 1
            current = q.get()
            row, col = lst[current]
            for v in range(count):
                if not visited[v]:
                    for k in range(4):
                        if lst[current][0] + dist_row[k] == lst[v][0] and lst[current][1] + dist_col[k] == lst[v][1]:
                            q.put(v)
                            visited[v] = True

print(c)
print(*sorted(counts.values()), sep="\n")

# q = queue.Queue()
# for i in range(n):
#     temp = input()
#     for j in range(n):
#         if temp[j] == "1":
#             lst.append((i, j))
# current = 0
# c = 0
# counts = {}
#
# while c < len(lst):
#     if q.empty():
#         current += 1
#         counts[current] = 0
#         q.put(lst.pop())
#
#     c += 1
#     row, col = q.get()
#     counts[current] += 1
#     for i in range(4):
#         new_row = row + dist_row[i]
#         new_col = col + dist_col[i]
#         if (new_row, new_col) in lst:
#             q.put((new_row, new_col))
#
# print(counts)