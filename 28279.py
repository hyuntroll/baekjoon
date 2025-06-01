import sys; input = sys.stdin.readline
from collections import deque
stack = deque()



for i in range(int(input())):
    s = input().split()


    # print(s)
    if "1" == s[0]:
        stack.appendleft(s[1])

    elif "2" == s[0]:
        stack.append(s[1])

    elif "3" == s[0]:
        # if len(stack) != 0 :
        #     stack.pop()
        print(stack.popleft() if stack else -1)
    
    elif "4" == s[0]:
        # if len(stack) != 0 :
        #     stack.pop()
        print(stack.pop() if stack else -1)
    
    elif "5" == s[0]:
        print(len(stack))
    
    elif "6" == s[0]:
        print(1 if not stack else 0)

    elif "7" == s[0]:
        # if len(stack) != 0 :
        #     stack.pop()
        print(stack[0] if stack else -1)
    
    elif "8" == s[0]:
        # if len(stack) != 0 :
        #     stack.pop()
        print(stack[-1] if stack else -1)

    

    
