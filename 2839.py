n = int(input())
lst = []
for i in range(1, n//3+1):
    if (n - 3*i) % 5 == 0:
        lst.append(i+(n-i*3)//5)

try:
    print(min(lst))
except:
    print(-1)

def test(n):
    ans = []
    if 0 == n%5:
        return n//5
    else:
        for i in range(0,(n//5)+1):
            if (n-i*5)%3 == 0:
                ans.append((n-i*5)//3 + i)
    return min(ans) if ans != [] else -1
print(test(n))