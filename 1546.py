n = int(input())
lst = list(map(int, input().split()))
a = sum([i/max(lst)*100 for i in lst])

print(a/n)