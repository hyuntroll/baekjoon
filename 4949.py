while True:
    s = input()
    if s == ".":
        break
    stack_a = []
    stack_b = []
    for i in s:
        if i == "[" or i == "(" :
            stack_a.append(i)
        elif i == ")" or i == "]":
            stack_b.append(i)
    






    # if len(stack)%2:
    #     print("bad")
    #     continue

    # while True:
    #     if len(stack) == 0:
    #         print("yes")
    #         break
        
    #     l, f = stack.pop(0), stack.pop()

    #     if not (l == "[" and f == "]") or (l == "(" and f == ")"):
    #         print("no")
    #         break

    # [ 다음 ]가 나올 때 까지 찾고 그 안에 (가 있으면 )가 나올 때 까지 찾음 없다면 No

    # (   [   )   ]


    