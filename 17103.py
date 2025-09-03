import sys; input = sys.stdin.readline
esa = [False, False] + [True]*(1000001-2) 
for i in range(2, 1000001):
    if esa[i]: 
        for k in range(2*i, 1000001, i): 
            esa[k] = False 
# print("Done")
for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2, n//2 +1):
        if esa[i] and esa[n-i]: 
            cnt +=1

    print(cnt)


# 에라토스는 다시 공부할 필요가 잇음 이부분에서 조금 설명해야 할 것들이 많은듯
# 에라토스는 다시 공부할 필요가 잇음 이부분에서 조금 설명해야 할 것들이 많은듯