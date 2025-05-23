n, k = map(int, input().split())


lst = list(range(1, n+1))
c = []
n = k

while lst:
    if n > len(lst):
        n = n -len(lst)
    else:
        c.append(str(lst.pop(n-1)))
        n += k -1
print(f"<{', '.join(c)}>")
    
# 이거는 다시 해봐야 할듯 