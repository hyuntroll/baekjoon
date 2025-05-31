import sys; input=sys.stdin.readline
sc = int(input())
stack = list(map(int, input().split()))
wait = []
cur = 1

while True:
    # print(stack, wait, cur)
    if len(wait) != 0:
        if wait[-1] == cur:
            wait.pop()
            cur +=1
        elif len(stack) != 0:
            wait.append(stack.pop(0))
        else:
            break

    elif len(stack) != 0:
        if stack[0] == cur:
            stack.pop(0)
            cur += 1
        else:
            wait.append(stack.pop(0))

        # if len(wait) != 0:
        #     if wait[-1] == cur:
        #         wait.pop()
        #         cur += 1
    elif len(wait) == 0:
        break        

    # else:
    #     if wait[-1] != cur:
    #         break
    
if len(wait) == len(stack):
    print("Nice")
else:
    print("Sad")
    