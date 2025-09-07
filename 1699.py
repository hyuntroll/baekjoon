import math as r

dp = [None] * 100001
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 1


def shittt(a, b):
    if dp[a] != None: return dp[a]
    if a == 0: return b

    arr = []
    for i in range(int(r.sqrt(a)), 0, -1):
        k = a
        k -= i**2; b +=1
        arr.append(shittt(k, b))

    dp[a] = min(arr) 
    return dp[a]

def abilityDp(a):
    if dp[a] != None: return dp[a]
    kkk = int(r.sqrt(a))
    if a == kkk**2:
        dp[a] = 1; return 1
    cnt = []

    for i in range(kkk, 0, -1):
        cnt.append(abilityDp(a-i**2) + 1)

    dp[a] = min(cnt)
    return dp[a]

print(abilityDp(int(input())))
# print(dp[0:51])
# print(shittt(int(input()) , 0))

"""

1 - 1
2 - 2 ( 1, 1 )
3 - 3 ( 1, 1, 1 )
4 - 1 (1, 1, 1, 1 | 2^2)
이전꺼 + 1, 아니믄 그전꺼 + 2?


25 < 27 -> dp{26} +1 

33 
dp[25] + dp[4] dp[4] -> 3 | dp[8] -> dp[4] + dp[4]
dp[16] + dp[16] + 1 -> 3
보면 25를 사용했음에도 저렇게 많이 걸림

dp돌려서 이전꺼 + n한거 중에 뭐가 가장 큰지?


"""

