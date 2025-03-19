import sys

input = sys.stdin.readline


N = int(input())


def test(n):
    ans = []
    if n % 5 == 0:
        return n // 5
    for i in range(0, n//5 + 1):
        if ( N - i * 5 ) % 3 == 0:
            ans.append(( N - i * 5) // 3 + i )
    
    return min(ans) if ans else -1

print(test(N))