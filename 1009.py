import sys; input = sys.stdin.readline
for _ in range(int(input())):
    a, b = map(int, input().split())
    k = b%4 if b%4 != 0 else 4 # 주기
    if a % 10 != 0:
        print((a**k)%10)
    else:
        print(10)

    # print(a**(b%4)%10)
    # for i in range(1, b+1):
    #     print((a**i)%10) -> 결국 이걸 보면 최대 4주기를 띄는 것을 알 수 있음
    # print( n if n else 10) -
#

# for i in range(1, 101):
#     for k in range(1, 6):
#         print((i**k)%10, end=" ")
#     print()
#     print()