cnt = None
def recursion(s, l1 ,l2):
    global cnt
    cnt += 1
    if l1 >= l2: # 이 전까지 모두 같았다는 뜻이므로 참 / l1 l2가 같으면 같은 값을 가리키고 이전까지 모두 같았으므로 참
        return 1
    elif s[l1] != s[l2]:
        return 0
    else:
        return recursion(s, l1+1, l2-1)

for _ in range(int(input())):
    cnt = 0
    n = input()
    print(recursion(n, 0, len(n)-1), cnt)


# 0 1 2 3


