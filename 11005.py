# ZZZZZ 36
# 수 ,  N진법
'''


자리수에 문자가 있으면 ord() 에서 -

A 아스키: 65  -> 10
Z 아스키: 90  -> 35

if 65 <= ord(문자) <= 90
    문자 - 55

'''


string, pns = map(int, input().split())
# pns = int(pns)

result_num = []

a = string

while True:
    a, b = divmod(a, pns)
    if 10 <= b:
        b = chr(b + 55)
    result_num.append(b)

    if a == 0:
        break

if result_num[-1] == 0:
    result_num.pop(-1)
result_num.reverse()
    

print(*result_num, sep='')

# string = 3

# mod = 4

# print(divmod(3, 4))