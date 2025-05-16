n = int(input())
s = input()
result = sum([  (ord(s[i])-96)*31**i for i in range(n)]  ) % 1234567891
print(result)


# 다른 언어로 풀어볼 필요가 있을 듯