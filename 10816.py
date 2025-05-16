n = int(input())

dit = {}
lst = list(map(int , input().split()))
for i in lst:
    if i not in dit:
        dit[i] = 1
    else:
        dit[i] += 1
input()
for k in list(map(int, input().split())):
    if k in dit:
        print(dit[k])
    else:
        print(0)
