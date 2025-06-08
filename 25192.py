n = int(input())


dit = {}
enter_flag = 0
cnt = 0
for _ in range(n):
    inp = input()
    if inp == "ENTER":
        enter_flag += 1
    else:
        if inp not in dit:
            dit[inp] = enter_flag
            cnt += 1
        elif dit[inp] != enter_flag:
            dit[inp] = enter_flag
            cnt += 1



print(cnt)
# for _ in range(n):
#     inp = input()
#     if inp == "ENTER":
#         if dit:
#             dit = {i: True for i in dit}
#     else:
#         if inp not in dit:
#             cnt +=1
#             dit[inp] = False
#         elif dit[inp]:
#             cnt +=1
#             dit[inp] = False 


# print(cnt)