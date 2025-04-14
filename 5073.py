while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    max_num = max(a, b, c)

    if a == b == c:
        print("Equilateral")
    elif a + b + c  - max_num > max_num:
        if len(set([a, b, c])) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")