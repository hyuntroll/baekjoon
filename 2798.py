creator = int(input())


for i in range(1, creator+1):
    num = sum(map(int, str(i))) + i
    if creator == num:
        print(i)
        break
else:
    print(0)