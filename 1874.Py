# '''
# 4 3 6 8 7 5 2 1





# '''


n = int(input())
lst = [int(input()) for _ in range(n)]
l = list(range(1, n+1))
stack = []
p = []
flag = False

while True:
    if len(stack) == 0:
        stack.append(l.pop(0))
        p.append("+")

    if stack[-1] == lst[0]:
        stack.pop()
        lst.pop(0)
        p.append("-")
    else:
        if len(l) == 0: # 왜냐하면 안맞아서 추가해야하는데 추가하고 싶어도 1 ~ n 수를 다 사용했기 때문에 정렬 불가 판단
            print("NO")
            break
        stack.append(l.pop(0))
        p.append("+")

    if len(lst) == 0:
        print("\n".join(p))
        break


# n = int(input())
# lst = [int(input()) for _ in range(n)]
# l = list(range(1, n+1))
# stack = []
# new = []
# flag = True
# while True:
#     if (len(stack) == 0):
#         stack.append(l.pop(0))
#         new.append("+")
#     elif stack[-1] == lst[0]:
#         stack.pop()
#         lst.pop(0)
#         new.append("-")
#     else:
#         stack.append(l.pop(0))
#         new.append("+")



    
    
# if not flag:
#     print("NO")
# else:
#     print("\n".join(new))