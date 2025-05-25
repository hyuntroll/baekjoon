from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    # 구할 거를 저장해서 루프 돌리다가 만약 그게 바로 프린트 안되면 뒤로 옮기기
    stack = deque()
    n, m = map(int, input().split())
    important = deque(list(map(int, input().split())))
    count = [0] * n

    idx = m
    pop = 0

    if n == 1:
        pop += 1
    else:
        while True:
            

            # print(important, idx)
            if important[0] != max(important):
                important.append(important.popleft())
            else:
                pop +=1
                important.popleft()
                if idx == 0:
                    break
            idx -= 1
            if idx < 0:
                idx = len(important) -1
    print(pop)
