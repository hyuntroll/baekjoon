N = int(input())
Sn = int(input())
S = input()

tup = tuple(i*2 for i in range(N+1))
count = 0
for i in range(0, Sn - (2*N +1) +1):
    flag = True
    for j in tup:
        if S[i+j] != "I":
            flag = False
            break
    if flag:
        count += 1

print(count)
#
# N = int(input())
# Sn = int(input())
# S = input()
#
# s = "I"
# new = "OI"
# string = s + (new * N)
# count = 0
# for i in range(0, Sn - (2*N +1) +1):
#     if S[i:i+2*N +1] == string:
#         count += 1
#
# print(count)