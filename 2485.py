

from math import gcd
import sys; input = sys.stdin.readline

lst = [int(input()) for _ in range(int(input()))]
# print([ lst[i] - lst[i-1] for i in range(1, len(lst))])
blank = [ lst[i] - lst[i-1] for i in range(1, len(lst))]
b_gcd = gcd(*blank)
cnt = 0
print(sum(i//b_gcd-1 for i in blank))


# b_gcd = gcd(*blank)
# bl = set(range(lst[0], lst[-1]+1, b_gcd))
# print(bl)
# print(len(bl - set(lst)))

#
#
#
#



# print(b_gcd)

# # for i in range(lst[0], lst[-1]+1, b_gcd):
# #     if i not in lst:
# #         lst.remove(i)


# # for i in range(1, int(sqrt(b_gcd)+1 )):
# # c = 0
# # for i in range(lst[0], lst[-1]+1, b_gcd):
# #     if i not in lst_s:
# #         c += 1
# # print(c)




# # lst = []
# # need = 0 

# # for i in range(int(input())):
# #     lst.append(int(input()))

# # print(blank)
# # print(gcd(min(blank), max(blank)))




# # 하나씩 띄울 땐 oXo, 2개씩 띄울 땐 oXXo, 2 +  
# # 큰 값이랑 작은값이랑 gcd
# # n = 1
# # print(list(range(2, 18, n +1)) )

# # # minb = min(blank)

# # # if not minb%2:
# # #     for i in blank:
# # #         if i == minb:
# # #             continue
# # #         else:
# # #             need += gcd(i, minb)
    

# # # print(need)