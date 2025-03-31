N = int(input())


lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))

if len(lst) == 1:
    print(0)
else:
    max_x = max(i[0] for i in lst)
    min_x = min(i[0] for i in lst)
    max_y = max(i[1] for i in lst)
    min_y = min(i[1] for i in lst)

    print((max_x-min_x) * (max_y-min_y))