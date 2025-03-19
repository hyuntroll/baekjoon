N, M = map(int, input().split())

n_lst = []
m_lst = []

sum_lst = []


for i in range(N):
    n_lst.append(list(map(int, input().split())))
for i in range(N):
    m_lst.append(list(map(int, input().split())))

for i in range(N):
    summ = []
    for k in range(M):
        summ.append(n_lst[i][k] + m_lst[i][k])
    sum_lst.append(summ)

for i in sum_lst:
    print(*i)