import sys; input = sys.stdin.readline
from collections import deque
stack = deque()



for i in range(int(input())):
    s = input()

    # print(s)
    if "push" in s:
        stack.append(s.split()[-1])
        # print(stack)

    elif "pop" in s:
        # if len(stack) != 0 :
        #     stack.pop()
        print(stack.popleft() if stack else -1)

    elif "front" in s:
        print(stack[0] if stack else -1)
    
    elif "back" in s:
        print(stack[-1] if stack else -1)

    elif "size" in s:
        print(len(stack))

    elif "empty" in s:
        print(1 if not stack else 0)
