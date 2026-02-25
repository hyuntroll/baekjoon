sudo = []
idx_list = []

row_check = [[False] * 10 for _ in range(9)]
col_check = [[False] * 10 for _ in range(9)]
box_check = [[False] * 10 for _ in range(9)]

for i in range(9):
    lst = list(map(int, input().split()))
    sudo.append(lst)
    for j in range(9):
        if lst[j] == 0:
            idx_list.append((i, j))
        else:
            num = sudo[i][j]
            row_check[i][num] = True
            col_check[j][num] = True
            box_check[(i//3) * 3 + (j//3)][num] = True

def sudof(idx):
    if idx == len(idx_list):
        return True

    i, j = idx_list[idx]
    b_i = (i//3) * 3 + (j//3)

    for num in range(1, 10):
        if not row_check[i][num] and not col_check[j][num] and not box_check[b_i][num]:
            row_check[i][num] = True
            col_check[j][num] = True
            box_check[b_i][num] = True
            sudo[i][j] = num

            if sudof(idx+1):
                return True

            row_check[i][num] = False
            col_check[j][num] = False
            box_check[b_i][num] = False
            sudo[i][j] = 0
    return False

sudof(0)
for i in range(9):
    print(*sudo[i])