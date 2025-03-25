n, a = map(int , input().split())

sort_lst = []

for i in range(n+1, 0, -1):
    if n % i == 0:
        sort_lst.append(n//i)
if len(sort_lst) < a:
    print(0)
else:
    print(sort_lst[a-1])