# import sys
# input = sys.stdin.readline

n, m = map(int, input().split())

pocket = {}
pocket_i = {}
for i in range(1, 1+n):
    s = input()
    pocket[s] = i
    pocket_i[i] = s


for i in range(m):
    s = input()
    if not s.isdigit():
        print(pocket[s])
    else:
        print(pocket_i[int(s)])