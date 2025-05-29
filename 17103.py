import sys; input = sys.stdin.readline
esa = [False, False] + [True]*(1000001-2) 
for i in range(2, 1000000 +1):
    if esa[i]: 
        for k in range(2*i, 1000000+1, i): 
            esa[k] = False 

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2, 1000000+1):
        if esa[i]:
            for j in range(i, 1000000+1):
                if esa[j]:
                    if i + j == n:
                        cnt +=1
    print(cnt)