n = int(input())
lst = []

# row, col, level
idx = [(0, 0, n)]

for _ in range(n):
    lst.append(input().split())
def is_full_filled(row, col, level): # True면 채워진거, False면 안채워진거 (잘라야함)
    color = lst[row][col]
    for i in range(row, row + level):
        for j in range(col, col + level):
            if color != lst[i][j]:
                return False
    return True
def slice_():
    blue = 0
    white = 0
    while len(idx) != 0:
        i, j, lv = idx.pop()

        if not is_full_filled(i, j, lv):
            lv = lv//2
            idx.append((i, j, lv))
            idx.append((i + lv, j, lv))
            idx.append((i, j + lv, lv))
            idx.append((i + lv, j + lv, lv))
        else:
            if lst[i][j] == "1":
                blue += 1
            else:
                white += 1
    return white, blue

print(*slice_(), sep="\n")