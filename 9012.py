def VPS(lst):
    type_stack = []
    for s in lst:
        if not type_stack and s == ")":
            return False
        elif s == "(":
            type_stack.append(1)
        else:
            # if s == ")":
            type_stack.pop()
    else:
        if type_stack:
            return False
        else:
            return True


n = int(input())
for i in range(n):
    stack = input()
    print("YES" if VPS(stack) else "NO")



