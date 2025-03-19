# 3 x 3 일 때
# ***
# * *
# ***

# N = 9
# ********* 1 i=1
# * ** ** * 2 i=1
# ********* 3 i=1
# ***   *** 1 i=2
# * *   * * 2 i=2
# ***   *** 3 i=2
# ********* 1 i=3
# * ** ** * 2 i=3
# ********* 3 i=3

N = 9

# print(" " * n)

# def buildstar(row, col, n):
#     if n == 3:
#         if row == 1 and col == 1:
#             print(" " * (n//3), end="")
#         else:
#             print("*", end="")
#     else:
#         a = n // 3
        
#         in_col = col
#         for i in range(a):
#             buildstar(row, k, a)
#             in_col += 1
        
def buildstar(row, col, n):
    pass  
'''
i, k일 때 언제인지 판단하게는 할 수 없나.

k가 n일때 3x3에선 n^인거를 나타내야하는데

그리고 row, col이 중앙부분이면 공백으로 <- 이거는 NxN일때 모두 실행

9x9일 때 작게 작게 나눠서 3x3으로 나타내서 별 표시하고, 
공백은 특정 숫자보다 작으면 공백 * 어떤 수


ㅗㅗㅗ
''' 

for i in range(N):
    for k in range(N):
        buildstar(i, k, N)
    print("")