import sys; input = sys.stdin.readline
esa = [False, False] + [True]*123455
for i in range(2, 123457):
    if esa[i]:
        for k in range(2*i, 123457, i):
            esa[k] = False



while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(1, n+1):
        if esa[i]:
            count += 1
#     count = 0
#     for i in range(n+1, n*2+1):
#         for k in range(2, int(i**(1/2))+1):
#             if not i % k:
#                 break
#         else:
#             count +=1
    print(count)