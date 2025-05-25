from collections import deque
import sys
input = sys.stdin.readline

# 구할 거를 저장해서 루프 돌리다가 만약 그게 바로 프린트 안되면 뒤로 옮기기
stack = deque()
n, m = 4, 2
important = deque([1, 2, 3, 4])
count = [0] * n

while len(important) > 1:
    if important[0] != max(important):
        important.append(important.popleft())
    else:
        important.popleft()