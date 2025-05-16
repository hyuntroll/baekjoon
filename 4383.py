
while True:
    try:
        n, *lst = map(int, input().split())
        if n == 1:
            print("Jolly")
        elif n >= 2:
            ran = list(range(1, n))
            check = []
            for i in range(1, n):
                s = int(abs(lst[i] - lst[i-1]))
                if s in ran:
                    check.append(s)



            if ran == sorted(check):
                print("Jolly")
            else:
                print("Not jolly")

        else:
            break
    except:
        break