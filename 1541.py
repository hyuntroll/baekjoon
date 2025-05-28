# s = input().split("-", maxsplit=1)
s=input().split("-")
# print(s)

# 괄호치는데는 제약이 없기 때문에 -로 나눠줘서 그값들 다 연산해서 빼주면 됨

#아니면 -발견되면 거기서부터 부호 반대로 해주면 될듯 / 또 -발견되면 거기서부터 다시하고 

def hap(lst):
    c = 0
    hapi = 0
    for i in range(0, len(lst)):
        # print(i)
        if lst[i] == "+":
            hapi += int( lst[c:i])
            # print(s[1][c:i])
            c = i+1
        elif i + 1 == len(lst):
            hapi += int(lst[c:])
    return hapi

hapi = hap(s[0])
for i in range(1, len(s)):
    hapi -= hap(s[i])
print(hapi)


string = input().split("-")
hapi = sum([int(i) for i in string[0].split("+")])
hapi -= sum([sum([int(k) for k in string[i].split("+")]) for i in range(1,len(string))])
print(hapi)

string = input().split("-")
hapi = sum(map(int, string[0].split("+")))
hapi -= sum(sum(map(int, k.split("+"))) for k in string[1:])
print(hapi)

# string = ['a', 'b', 'c', 'd']
# for i in string:
#     print("removing", i)
#     string.remove(i)

# c = 0
# hap = 0
# for i in range(0, len(s[0])):
#     # print(i)
#     if s[0][i] == "+":
#         hap += int( s[0][c:i])
#         # print(s[1][c:i])
#         c = i+1
#     elif i + 1 == len(s[0]):
#         hap += int(s[0][c:])

# c = 0
# hap_s = 0
# if len(s) == 2:

#     for i in range(0, len(s[1])):
#         # print(i)
#         if s[1][i] == "-" or s[1][i] == "+":
#             hap_s += int( s[1][c:i])
#             # print(s[1][c:i])
#             if s[1][i] == "-":
#                 c = i
#             else:
#                 c = i+1
#         elif i + 1 == len(s[1]):
#             hap_s += int(s[1][c:])
#             # print(s[1][c:])

# print(hap - hap_s)
# # print(s[1])

