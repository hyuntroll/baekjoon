inter = []

max_in_lst = 0
row = 0
col = 0

for i in range(9):
    inter.append(list(map(int, input().split())))
    if max(inter[i]) > max_in_lst:
        max_in_lst = max(inter[i])
        row = i
        col = inter[i].index(max_in_lst)
print(max_in_lst)
print(row+1, col+1)

