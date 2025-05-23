import sys
from collections import deque


input = sys.stdin.readline

stack = deque()
for i in range( int(input())):
    s = input()
    if "push" in s:

        stack.append(int(s.split()[1]))

    elif "top" in s:
        print(stack[-1] if stack else -1)

    elif "pop" in s:

        print(stack.pop() if stack else -1) 
    elif "size" in s:

        print(len(stack))
    elif "empty" in s:
        print(1 if not stack else 0)
