# 서로 다른 부분 문자열의 개수


s = input()

dit = {}

for i in range(len(s)):
    for j in range(len(s)-i):
        # print(s[i:j+i+1])
        if s[i:j+i+1] not in dit:
            dit[s[i:j+i+1]] = 0
        else:
            dit[s[i:j+i+1]] +=1
print(sum([1 for k in dit]))