def gcd(a, b):
    while True:
        r = a%b
        if r == 0:
            break
        a = b
        b = r
    return b

lst = []
need = 0 

for i in range(int(input())):
    lst.append(int(input()))

blank = [ lst[i] - lst[i-1] -1 for i in range(1, len(lst))]
print(blank)
print(gcd(min(blank), max(blank)))




# 하나씩 띄울 땐 oXo, 2개씩 띄울 땐 oXXo, 2 +  
# 큰 값이랑 작은값이랑 gcd
# n = 1
# print(list(range(2, 18, n +1)) )

# # minb = min(blank)

# # if not minb%2:
# #     for i in blank:
# #         if i == minb:
# #             continue
# #         else:
# #             need += gcd(i, minb)
    

# # print(need)