import sys; input = sys.stdin.readline
from collections import deque
stack = deque()



for i in range(int(input())):
    s = input()

    # print(s)
    if s[0] == "1":
        stack.append(s.split()[-1])
        # print(stack)

    elif "2" == s[0]:
        # if len(stack) != 0 :
        #     stack.pop()
        print(stack.pop() if stack else -1)

    elif "5" == s[0]:
        print(stack[-1] if stack else -1)

    elif "3" == s[0]:
        print(len(stack))

    elif "4" == s[0]:
        print(1 if not stack else 0)
