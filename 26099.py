import sys

input = sys.stdin.readline


N = int(input())


def test(n):
    # ans = []
    if n % 5 == 0:
        return n // 5
    for i in range(n//5, -1, -1):
        if ( N - i * 5 ) % 3 == 0:
            return ( N - i * 5) // 3 + i
    # for i in range(n//5+1, 0):
    
    return -1

print(test(N))


# 다른 풀의

cnt = 0

while N > 0:
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    
    N -= 3
    cnt += 1
else:
    print(-1)