N = int(input())
lst = list(map(int, input().split()))
op_n = list(map(int, input().split()))
op = []
for i in range(len(op_n)):
    for k in range(op_n[i]):
        if (i == 0):
            op.append('+')
        elif ( i == 1):
            op.append('-')
        elif ( i == 2):
            op.append('*')
        else:
            op.append('/')
    
# print(op)

combi = [0] * len(op)
sum_lst = []

def bf( start, depth, used_lst):
    abc = used_lst[:]
    if depth == N-1:
        # print(combi)
        summ = lst[0]
        for i in range(1, N):
            # if combi.count(combi[i-1]) != op.count(combi[i-1]):
                # break
            if combi[i-1] == "+":
                summ += lst[i]
            elif combi[i-1] == "-":
                summ -= lst[i]
            elif combi[i-1] == "*":
                summ *= lst[i]
            else:
                summ = summ // lst[i] if ( abs(summ) == summ and abs(lst[i]) == lst[i] )or (abs(summ) != summ and abs(lst[i]) != lst[i]) else -1 * (abs(summ)//abs(lst[i]) )
            # print(f"엄; {combi} {summ}")
            sum_lst.append(summ)
            # print(summ)
        # print("리떤")
        return
    for i in range(start, N-1):
        if i not in abc:
            combi[depth] = op[i] # 전에 했던건 하지 안되, 다른건 넣을 수 있음 
            abc.append(i)
            bf(0, depth+1, abc[:])
        else:
            return

bf(0, 0, [])

print(max(sum_lst))
print(min(sum_lst))
