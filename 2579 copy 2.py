# # # DP문제 그럼 이전에 올라왔던 숫자를 기억하면서 한칸을 갔을 때 보다 두칸을 갔을 때 더 많은지 체크
# import sys; input=sys.stdin.readline

# n = int(input())

# max_score = 0

# stair_weight = []

# dp = []

# for i in range(n):
#     stair_weight.append(int(input()))


# def find(i, repeat_count, score):
#     global max_score
#     # print(i, repeat_count, score)

#     if i == len(stair_weight) -1:
#         max_score = max(score + stair_weight[i], max_score)
#         return
#     if i > len(stair_weight) -1:
#         return

#     score += stair_weight[i]

#     if repeat_count != 1 and i <= len(stair_weight) -2:
#         find(i+1, repeat_count+1, score) # 한칸
#     if i <= len(stair_weight) -3:
#         find(i+2, 0, score) # 두칸

# find(0, 0, 0)
# find(1, 0, 0)
# print(max_score)