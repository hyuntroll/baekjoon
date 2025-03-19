N = int(input())
lst = (list(map(int, input().split())))

sum_lst = []
combi = []

def bfs(start, depth):
    if depth == len(combi):
        # print(combi, sum_lst)
        # if len(sum_lst) == 0:
        #     sum_lst.append(sum(combi))
        # elif sum(combi) - sum_lst[-1] > 1:
        #     result = sum_lst[-1] + 1 
        # else:
        sum_lst.append(sum(combi))
        return 
    for i in range(start, N):
        combi[depth] = lst[i]
        bfs(i+1, depth+1)

for i in range(1, N+1):
    combi = [0] * i
    bfs(0, 0)

sum_lst.sort()


# print(sum_lst)
for i in range(0, len(sum_lst)):
    # print(sum_lst[i] - sum_lst[i-1])
    if i == 0: 
        if sum_lst[i] > 1:
            print(1)
            break
        else:
            continue
    if sum_lst[i] - sum_lst[i-1] > 1:
        print(sum_lst[i-1] +1)
        break
else:
    print(sum_lst[-1] +1)

