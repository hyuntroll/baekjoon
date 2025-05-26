dp = [0] * 41
def fibo(n):
    if n == 0:
        c[n] += 1
        return 0
    elif n == 1:
        c[n] += 1
        return 1
    elif dp[n] != 0:
        return dp[n-1]
    else:
        dp[n] = fibo(n-1) + fibo(n-2)
        return dp[n]

        
for _ in range(int(input())):
    c = [0, 0]
    fibo(int(input()))
    print(*c)