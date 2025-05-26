import sys; input=sys.stdin.readline

zl = [0] * 41
ol = [0] * 41
zl[0] = 1; zl[1] = 0
ol[0] = 0; ol[1] = 1

for i in range(2, 41):
    zl[i] = zl[i-1] + zl[i-2]
    ol[i] = ol[i-1] + ol[i-2]

for _ in range(int(input())):
    n = int(input())
    print(zl[n], ol[n])

# zero랑 one이 몇번 출력되는지만 구해서 | 값에 맞는 0, 1 개수를 출력한다 -> 더하면 값이 나옴 ㅇㅇ

dp = [0] * 41
zl = [0] * 41
ol = [0] * 41
dp[0] = 0; dp[1] = 1
zl[0] = 1; zl[1] = 0
ol[0] = 0; ol[1] = 1

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] != 0:
        return dp[n]
    else:
        dp[n] = fibo(n-1) + fibo(n-2)
        zl[n] = zl[n-1] + zl[n-2]
        ol[n] = ol[n-1] + ol[n-2]
        return dp[n]

for _ in range(int(input())):
    n = int(input())
    fibo(n)
    print(zl[n], ol[n])