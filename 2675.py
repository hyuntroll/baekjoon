T = int(input())


for i in range(T):
    intu= input()
    a = int(intu[0])
    lst = intu[2:]
    print("".join([str(i) * a for i in lst]))
