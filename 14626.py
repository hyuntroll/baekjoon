ISBN = input()

hap = 0
m = 0
star = 0
weight = 0

if ISBN[-1] == "*":
    for index, e in enumerate(ISBN[:-1]):
        if index%2 == 0:
            hap += int(e)
        else:
            hap += int(e)*3

    m = (10 - hap%10)%10
    print(m)

else:
    for index, e in enumerate(ISBN[:-1]):
        if e == "*":
            weight = 1 if index%2 == 0 else 3
        else:
            if index%2 == 0:
                hap += int(e)
            else:
                hap += int(e)*3
    

    m = int(ISBN[-1])
    for i in range(0, 10):
        if (10 - (hap+i*weight)%10)%10 == m:
            print(i)
            break