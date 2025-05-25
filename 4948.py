import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for i in range(n+1, n*2+1):
        for k in range(2, int(i**(1/2))+1):
            if not i % k:
                break
        else:
            count +=1
    print(count)