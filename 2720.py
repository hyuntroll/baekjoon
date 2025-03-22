repeat = int(input())

for i in range(repeat):
    N = int(input()) * 10
    # print(N)

    current_check = 0
    mon_lst = [250, 100, 50, 10]
    c_lst = [0, 0, 0, 0 ]# 0.25, 0.10, 0.05, 0.01

    while N != 0:
        if N >= mon_lst[current_check]:
            N -= mon_lst[current_check]
            c_lst[current_check] += 1
        
        else:
            current_check += 1

    print(*c_lst)