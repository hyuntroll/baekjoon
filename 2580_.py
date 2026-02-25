sudo = []
idx_list = []
dist = (0, 3, 6)

for i in range(9):
    lst = list(map(int, input().split()))
    sudo.append(lst)
    for j in range(9):
        if lst[j] == 0:
            idx_list.append((i, j))

def sudof(idx):
    if idx == len(idx_list):
        return True

    i, k = idx_list[idx]
    for j in range(1, 10):
        if j in sudo[i]:
            continue

        flag = False
        for z in range(9):
            if j == sudo[z][k]:
                flag = True
                break
        if flag:
            continue

        di = dist[i//3]
        dk = dist[k//3]
        for u in range(di, di+3):
            for v in range(dk, dk+3):
                if sudo[u][v] == j:
                    flag = True
                    break
                if flag: break
        if flag:
            continue

        sudo[i][k] =j
        if sudof(idx+1):
            return True
        sudo[i][k] = 0

    return False


for i in range(len(idx_list)):
    sudof(i)
for i in range(9):
    print(*sudo[i])