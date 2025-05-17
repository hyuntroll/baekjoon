lst = []


n = int(input())
for i in range(n):
    lst.append(list(map(int, input().split())))
# _sorted = sorted(lst, key=lambda x: x[1], reverse=True)
cur = [0] * n
# print(sorted_)
grade = 1
for i in range(n):
    grade = 1
    neo = lst[i]
    for k in lst:

        if neo[1] < k[1] and neo[0] < k[0]:

            grade +=1
    print(grade)



# for i in range(n-1):
#     if sorted_[i][1] != sorted_[i+1][1] and sorted_[i][0] > sorted_[i+1][0]: 
#         cur[lst.index(sorted_[i])] = grade
#         grade = len(sorted_[:i+2]) +1
#     else:
#         cur[lst.index(sorted_[i])] = grade

#     cur[lst.index(sorted_[i+1])] = grade


# print(*cur)



# # print(sorted_)
# # for i in range(n-1):
# #     # print(sorted_[i+1][0], sorted_[i][0])
# #     if sorted_[i+1][0] < sorted_[i][0]:
# #         grade = i+1
# #         k = grade
# #         if not cur[lst.index(sorted_[i])]:
# #             cur[lst.index(sorted_[i])] = grade
# #     else:
# #         cur[lst.index(sorted_[i+1])] = k
# #         cur[lst.index(sorted_[i])] = k
    

# # if sorted_[n-1][0] < sorted_[n-2][0]:
# #     grade = n
# # cur[lst.index(sorted_[n-1])] = grade

# # print(*cur)