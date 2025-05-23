lst = ["(", "[", ")", "]"]

while True:
    type_stack = []
    stack = input()
    if stack == ".":
        break
    for s in stack:
        if s not in lst:
            continue
        if not type_stack:
            if s == "(" or s == "[":
                type_stack.append(1 if s == "(" else 2)
            else:
                print("no")
                break
        elif s == "(" or s == "[":
                type_stack.append(1 if s == "(" else 2)
        else:
            if s == "]" and type_stack[-1] == 2 or s == ")" and type_stack[-1] == 1:
                type_stack.pop()
            else:
                print("no")
                break
    else:
        if type_stack:
            print("no")
        else:
            print("yes")


# # while True:
# s = input()
# # if s == ".":
# #     break
# stack_a = []
# stack_b = []
# stack = []
# for i in s:
#     if i == "[" or i == "(" :
#         stack_a.append(i)
#         stack.append(i)
#     elif i == ")" or i == "]":
#         stack_b.append(i)
#         stack.append(i)
# print(stack)
# print(stack_a)
# print(stack_b)

# # stack = ['(', ']']
# type_stack = [] # 1 = (), 2 = [] 마지막 인덱스를 가지고 판단함

# for s in stack:
#     # print(type_stack)
#     if not type_stack:
#         if s == "(" or s == "[":
#             type_stack.append(1 if s == "(" else 2)
#         else:
#             print(False)
#             break
#     elif s == "(" or s == "[":
#             type_stack.append(1 if s == "(" else 2)
#     else:
#         if s == "]" and type_stack[-1] == 2 or s == ")" and type_stack[-1] == 1:
#             type_stack.pop()
#         else:
#             print(False)
#             break
# if type_stack:
#     print(False)
# else:
#     print(True)


#     # if len(stack)%2:
#     #     print("bad")
#     #     continue

#     # while True:
#     #     if len(stack) == 0:
#     #         print("yes")
#     #         break
        
#     #     l, f = stack.pop(0), stack.pop()

#     #     if not (l == "[" and f == "]") or (l == "(" and f == ")"):
#     #         print("no")
#     #         break

#     # [ 다음 ]가 나올 때 까지 찾고 그 안에 (가 있으면 )가 나올 때 까지 찾음 없다면 No

#     # (   [   )   ]


    