m, n = map(int, input().split())
for i in range(m, n+1):
    if i == 1:
        continue
    for k in range(2, int(i**(1/2))+1):
        if not i % k:
            break
    else:
        print(i)