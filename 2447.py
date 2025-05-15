# 3 x 3 일 때
# ***
# * *
# ***

# N = 9
# ********* 1 i=1 k=1
# * ** ** * 2 i=1 k=2
# ********* 3 i=1 k=3
# ***   *** 1 i=2 k=1
# * *   * * 2 i=2 k=2
# ***   *** 3 i=2 k=3
# ********* 1 i=3 k=1
# * ** ** * 2 i=3 k=2
# ********* 3 i=3 k=3

N = 9

column_9 = 0
for column_3 in range(3):
    if column_3 == 1: # 이 부분을 바꿔주기
        print("* *" *(3//3))
    else:
        print("***" *(3//3))

# 행 열 | 전부 하나 만드는데 사용 ㅇㅇ i = 1 쪽에 있을 때 중앙에 공백



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



# column이 N에서 시작하는거랑 N//3 에서 시작하는거랑 --- 만들어서
# 그 부분이 되면 column에 맞는걸로 해서 ㅇㅇ

stars = ["***", "* *", "   "]

N = 9
column = 0
# range에 값이 3이 될때까지 재귀, 아니면 1이 
for i in range(N//3):
    for j in range(N//9):
        print(stars[0], end="")
print()

column += 1
for i in range(N//3):
    pass




# 3 x 3 일 때
# ***
# * *
# ***


# 3x3 __col, __row
# 9x9 _col, _row
# __col = 0, __row = 0, _col = 0, _row = 0
# *********
# __col = 1, __row = 0, _col = 0, _row = 0
# * ** ** * 

#
# N = 9
# ********* 1 i=1 k=1
# * ** ** * 2 i=1 k=2
# ********* 3 i=1 k=3
# ***   *** 1 i=2 k=1
# * *   * * 2 i=2 k=2
# ***   *** 3 i=2 k=3
# ********* 1 i=3 k=1
# * ** ** * 2 i=3 k=2
# ********* 3 i=3 k=3

print("\n\n\n\n\n\n\n")




# def buildStar(n, col, row):
#     if ( n != 3 ):
#         # print("\n", col, row)
#         if ( n//3 -1 < col%3 < n//3 - n//3) and (n//9 -1 < row%3 < n//3 - n//9):
#             print("   " * (n//3), end="")
#         else:
#             for _col in range(col//3):
#                 buildStar(n//3, col//3, row//3)
#     else:
#         if ( col != 1):
#             print("***", end="")
#         else:
#             print("* *", end="")



def rowStar(n, col, row):
    if n != 3:
        rowStar(n//3, col//3, row//3)
    else:
        if col == 1 and row == 1:
            print(" ", end="")
        else:
            print(col, end="")


def colStar(n, col, row):
    if n != 3:
        colStar(n//3, col//3, row//3)
    else:
        if col == 1 and row == 1:
            print(" ", end="")
        else:
            print("*", end="")

# row col pre 모두 합치면 될듯

def preStar(n, col, row):
    if n != 3:
        preStar(n//3, col%3, row%3)
    else:
        if col == 1 and row == 1:
            print(" ", end="")
        else:
            print(col, end="")

def buildStar(n, col, row, _col, _row):
    if col % 3 != 1 and row % 3 != 1:
        buildStar(n//3, col%3, row%3, _col//3, _row//3)
    else:
        if n == 1:
            print("*", end="")
        else:
            print(" ",)

N = 27
# for col in range(N):
#     for row in range(N):
#         preStar(N, col, row)
#     print()
# print()
# for col in range(N):
#     for row in range(N):
#         # print("*", end="")
#         rowStar(N, col, row)
#     print()
# print()
# for col in range(N):
#     for row in range(N):
#         # print("*", end="")
#         colStar(N, col, row)
#     print()

# print()
for col in range(N):
    for row in range(N):
        buildStar(N, col, row, col, row) # 현재 작은거 뭐를 만들고 있는지
    print()




def fuck(col, row, n):
    if n == 1:
        print("*", end="")
        return
    
    if col % 3 == 1 and row % 3 == 1:
        print(col, end="")
        return
    
    fuck(col // 3, row // 3, n // 3)

for col in range(N):
    for row in range(N//3):
        fuck(col, row, N)
    print()

def is_blank(x, y):
    while x > 0 and y > 0:
        if x % 3 == 1 and y % 3 == 1:
            return True
        x //= 3
        y //= 3
    return False

N = 27
for i in range(N):
    for j in range(N):
        print(" " if is_blank(i, j) else "*", end="")
    print()


# 무조건 다시 푼다