import sys
input = sys.stdin.readline
def lol(x):
    return int(x + 0.5)

n = int(input())
a = lol((n * 0.15))
# print(a)
lst = []

for i in range(n):
    lst.append(int(input()))

print(   lol(sum(sorted(lst)[a: n -a ])/(n-2*a)    ) if n != 0 else 0)



# 1 5 5 7 8