while True:
    n = int(input())
    if n == -1:
        break

    sort_lst = []

    for i in range(n, 1, -1):
        if n % i == 0:
            sort_lst.append(n//i)

    if sum(sort_lst) == n:
        print(f"{n} = ", end="")
        print(*sort_lst, sep=" + ")
    else:
        print(f"{n} is NOT perfect.")