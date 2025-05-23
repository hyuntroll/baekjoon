import sys
from collections import deque


input = sys.stdin.readline

queue = deque()
for i in range( int(input())):
    s = input()
    if "push" in s:

        queue.append(int(s.split()[1]))

    elif "pop" in s:

        print(queue.popleft() if queue else -1) 
    elif "size" in s:

        print(len(queue))
    elif "empty" in s:
        print(1 if not queue else 0)
    elif "front" in s:
        print(queue[0] if queue else -1)
    elif "back" in s:
        print(queue[-1] if queue else -1)
