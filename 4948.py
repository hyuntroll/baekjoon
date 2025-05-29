import sys; input = sys.stdin.readline
esa = [False, False] + [True]*246913 # 일단 0 , 1 제외 모든 수를 소수라 가정
for i in range(2, 246913):
    if esa[i]: # 숫자라 소수로 되어있다면
        for k in range(2*i, 246913, i): # 그 수의 2배부터는 모두 다 소수가 아님 (i의 배수는 모두 소수가 아님)
            esa[k] = False  # 그래서 i의 배수들은 모두 False처리

# 1 ~ 246912 1 246912+1 -2
  
while True:
    n = int(input().strip())
    if n == 0:
        break
    count = 0

    for i in range(n+1, 2*n+1):
        # print("a", i)
        if esa[i]:
            count += 1

    print(count)


#     count = 0
#     for i in range(n+1, n*2+1):
#         for k in range(2, int(i**(1/2))+1):
#             if not i % k:
#                 break
#         else:
#             count +=1


