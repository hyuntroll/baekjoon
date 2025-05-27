# DP문제 그럼 이전에 올라왔던 숫자를 기억하면서 한칸을 갔을 때 보다 두칸을 갔을 때 더 많은지 체크
import sys; input=sys.stdin.readline

def find(n, *lst):
    return "fuckyou"

        


n = int(input())
print(find(n, *[int(input()) for _ in range(n)]))



# 1 2 3 4 5



    # stairs = 1
    # cnt = 1
    # DP = [0] * (n+1)
    # DP[1] = lst[0]
    # for i in range(1, n):
    #     DP[i] = DP[i] + lst[i] 
    #     if stairs == 2:
    #         print("new")
    #         DP[i] = DP[i] + lst[i+1]
    #         stairs = 1
    #     elif n-2 == 3 and stairs == 1:
    #         print("newthing")
    #         DP[i] = DP[i] + lst[i+1]
    #         break
    #     else:
    #         print(DP[i], DP[i] +lst[i+1])
    #         DP[i] = max(DP[i], DP[i] +lst[i+1])
            
    #         stairs += 1 if DP[i] > DP[i] +lst[i+1] else 0
    #         print(stairs)
    #     cnt += stairs

    #     if cnt == n:
    #         break