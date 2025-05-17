def fact(a):
    cur = 1
    for i in range(1, a+1):
        cur *= i
    return cur

cu = 0
for i in reversed(str(fact(int(input())))):
    if i == "0":
        cu += 1
    else:
        break
print(cu)

# 뒤에서부터 0 안나올때까지 찾는거 ㅇㅇ;