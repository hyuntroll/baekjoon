
# import sys
# input = sys.stdin.readline

# lst = list(range(1, int(input())+1))

# while len(lst) != 1:
#     lst.pop(0)
#     lst.append(lst.pop(0))
# print(lst[0])

# # 다시  


from collections import deque
import sys
input=sys.stdin.readline
que = deque(list(range(1, int(input())+1)))
while len(que) != 1:
    # print(que)
    que.popleft()
    que.append(que.popleft())
print(que[0])
