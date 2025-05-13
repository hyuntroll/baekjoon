while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
        break

    max_num = lst.pop(lst.index(max(lst)))

    print("right" if sum([i**2 for i in lst]) == max_num**2 else "wrong")