from collections import deque
import sys; input=sys.stdin.readline
n = int(input())
deq = list(map(int, input().split()))

# n = 5
# deq = [3, 2, 1, -3, -1]
d_i = list(range(1, n+1))
idx = 0


def bob(i):
    global deq, idx

    idx += deq[i]
    if deq[i] > 0:
        idx -= 1 # 빼주는 이유는 앞에꺼가 빠지는 경우가 있기 때문에 하나 더 빼야지 찾으려는 idx가 됨

    # print("i", deq.pop(i))
    deq.pop(i)
    print(d_i.pop(i), end=" ")
    # print(deq.pop(i))

    if len(deq) == 0:
        return False

    while True:
        if idx < 0:
            idx += len(deq)
        elif idx >= len(deq):
            idx -= len(deq)
        else:
            break
    
    # print("next:", idx)


for i in range(n):
    bob(idx)
# bob(2)
# bob(2)
# bob(1)
# bob(0)
# print(deq)
