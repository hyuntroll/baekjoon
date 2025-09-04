# # # DP문제 그럼 이전에 올라왔던 숫자를 기억하면서 한칸을 갔을 때 보다 두칸을 갔을 때 더 많은지 체크
## 가장 위에서 부터 아래쪽으로 내려가기로 결정
import sys; input=sys.stdin.readline

n = int(input())

max_score = 0

arr = []

dp = [0] * n ## 여기서 dp는 각 위치에서 얻을 수 있는 최대 스코어

for i in range(n):
    arr.append(int(input()))

def find(idx):
    if idx == 0: # 가장 첫번 째는 dp가 가중치와 같음
        dp[idx] =  arr[idx]
    elif idx == 1: # 두번 째에서는 얻을 수 있는 가장 큰값이 첫번 째 + 두번 째 가중치임
        dp[idx] = dp[idx-1] + arr[idx]
    elif idx == 2: # 세번 째부터는 3칸전에서 두번 뛴 후 한칸 올라오는 경우(그러면 연속 두번까지), 아니면 두칸 뒤에서 점프해서 도달하는 경우 <- 이 두 경우밖에 성립되지 않음
        dp[idx] = max(dp[idx-2], arr[i-1]) + arr[idx]
    else: # 마찬가지 | 3칸 전에서 두칸 뛰었을 때는 3칸은 dp로 그다음 칸은 가중치로 둬야함 (dp는 최대 스코어 이기 때문)
        dp[idx] = max(dp[idx-3] + arr[i-1], dp[idx-2]) + arr[idx]

for i in range(n):
    find(i)

print(dp[-1])