import sys; input= sys.stdin.readline

def findOne(n):
    dp = [0] * (n+1)
#   dp[0] ,[1] 들어가는데 dp[x]는 x값을 위한 최소 연산 / dp[1]은 이미 값이 1 이므로 연산할 필요가 없음
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1 # -1 했을 때

        if not i % 2: # -1 했을때랑 2로 나눴을 때 비교 
            dp[i] = min(dp[i//2]+1, dp[i]) 
        if not i % 3: # -1했을때랑 3로 나눴을 때 비교
            dp[i] = min(dp[i//3]+1, dp[i])

        # i//2인 이유는 이전 값에서 2를 곱해서 현재 수가 나왔기 때문에 이전수가 얼마만큼 연산했는지를 알고
        # 그 값과 -1를 했을 때를 비교해서 최소값을 구하는 것

    return dp[n]

print(findOne(int(input())))