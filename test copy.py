lst = []

N, M = map(int, input().split())
for _ in range(M):
    lst.append(input().split())
st, ed = input().split()

min_s = []

for i in [lst.index(i) for i in lst if i[0] == st]:
    k = lst[i][1]
    while True:
        s = int(lst[i][2])
        if len([j for j in lst if j[0] == k]) == 0:
            break
        for j in [lst.index(j) for j in lst if j[0] == k]:
            s += int(lst[j][2])
            k = lst[j][1]
            if k == ed:
                break
        if k == ed:
            min_s.append(s)
            break
print(min(min_s) if len(min_s) != 0 else -1)