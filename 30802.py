n = int(input())
lst = list(map(int, input().split()))
T, P = map(int,input().split())

ts = 0
for t in lst:
    ts += 1 + t//T if t%T != 0 else t//T
print(ts)
print(n//P, n%P)