import sys

input = sys.stdin.readline

lst = []


for i in range(int(input())):
    a, b = map(int, input().split())
    lst.append([a, b])

lst.sort(key = lambda x: (x[0], x[1]))

for i in lst:
    print(*i, sep=" ")