# ZZZZZ 36
# 수 ,  N진법
'''


자리수에 문자가 있으면 ord() 에서 -

A 아스키: 65  -> 10
Z 아스키: 90  -> 35

if 65 <= ord(문자) <= 90
    문자 - 55

'''


string, pns = input().split()
pns = int(pns)

result_num = 0

for i in range(len(string)-1, -1, -1):
    # print(ord(string[i]), string[i], i)
    if 65 <= ord(string[i]) <= 90:
        result_num += ( ord(string[i]) - 55 ) * pns**(len(string)-1-i)
    else:
        result_num += int(string[i]) * pns**(len(string)-1-i)
print(result_num)