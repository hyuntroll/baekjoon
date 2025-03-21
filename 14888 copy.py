N = int(input())
lst = list(map(int, input().split()))
op_n = list(map(int, input().split())) 
combi = [0] * (N-1)
visited = [0] * 4
sum_lst = []

def bf( start, depth ):


    if depth == N-1:
        # print(*combi)

        combi_sum = lst[0]

        for i in range(1, N):
            if combi[i-1] == "+":
                combi_sum += lst[i]
            elif combi[i-1] == "-":
                combi_sum -= lst[i]
            elif combi[i-1] == "*":
                combi_sum *= lst[i]
            else:
                combi_sum = combi_sum // lst[i] if ( abs(combi_sum) == combi_sum and abs(lst[i]) == lst[i] )or (abs(combi_sum) != combi_sum and abs(lst[i]) != lst[i]) else -1 * (abs(combi_sum)//abs(lst[i]) )
            
        sum_lst.append(combi_sum)

        return
    
    for i in range(start, 4):

        if visited[i] != op_n[i] and op_n[i] != 0:
            visited[i] += 1
            if i == 0:
                combi[depth] = "+"
            elif i == 1:
                combi[depth] = "-"
            elif i == 2:
                # print("아니 ;")
                combi[depth] = '*'
            else:
                combi[depth] = '/'
            
            bf(0, depth+1)

            visited[i] -= 1

bf(0, 0)

print(max(sum_lst))
print(min(sum_lst))

