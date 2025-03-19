lst = list(map(int, input().split()))

# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
# 0 1 2 2 2 7



print(1 - lst[0], 1 - lst[1], 2 - lst[2], 2 - lst[3], 2 - lst[4], 8 - lst[5])