n = int(input())
lst = list(map(int, input().split()))

count = 1
for i in range(n):
    for j in range(i+2, n+1):
        sliced = lst[i:j]
        if len(set(sliced)) >= 3:
            break
        length = len(sliced)
        if count < length:
            count = length

print(count)