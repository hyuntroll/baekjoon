# 5개일 때

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

N = int(input())


for i in range(N):
    print(" " * (N-1 - i), end="")
    print("*" * ((i + 1) * 2 - 1))
for i in range(N-2, -1, -1):
    print(" " * (N-1 - i), end="")
    print("*" * ((i + 1) * 2 - 1))



for i in range(N+N-1): # 중간꺼는 한번만 출력되니까 -1
    for k in range(abs(N-i-1)): # 이 뜻이 뭐나하면 원래는 현재 index에서 -1만큼 공백을 출력해야함 근데 N이랑 index가 같으면 음수가 되니까 절댓값으로
        print(" ", end="")
    for j in range((N - abs(N-i-1))*2-1): # 이놈은 0일 때 1, 1일 때 3이 나와야 하는데 (index+1)*2 - 1 해야 나오는데 위랑 비슷하게 지랄나면 좆돼서 ㅇㅇ;
        print("*", end="")
    print("")


