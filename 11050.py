def fact(a):
    cur = 1
    for i in range(1, a+1):
        cur *= i
    return cur
n, k = map(int, input().split())
print(fact(n)//(fact(n-k) * fact(k)))