N = int(input())

lst_ld = []

for i in range(N):
    left, down = map(int, input().split())
    lst_ld.append((left, down))
    