lst = []
for _ in range(int(input())):
    lst.append(input())
lst = list(set(lst))

lst.sort()
lst.sort(key= lambda x: len(x))

print(*lst, sep="\n")