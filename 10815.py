import sys
input = sys.stdin.readline

N = int(input())
nlst = list(map(int, input().split()))
M = int(input())

mlst = map(int, input().split())

_dict = {}
for i in nlst:
    _dict[i] = 0

for j in mlst:
    print(int(j in _dict), end=" ")

# dictionary를 사용하면 더 빠름