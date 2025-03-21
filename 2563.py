N = int(input())

lst_ld = []
lst_rp = []

for i in range(N):
    left, down = map(int, input().split())
    lst_ld.append((left, down))
    lst_rp.append((left+10, down +10))

# for i in range(N):
#     for k in range(N):
#         if lst_ld[i][0] < lst_ld[k][0] < lst_rp[i][0]:
#             if lst_ld[i][1] < lst_ld[k][1] < lst_rp[i][1]:
#                 # print(lst_ld[k])
#             if lst_ld[i][1] < lst_rp[k][1] < lst_rp[i][1]:
#                 # print(lst_ld[k], "b", i, k)
#         if lst_ld[i][0] < lst_rp[k][0] < lst_rp[i][0]:
#             if lst_ld[i][1] < lst_ld[k][1] < lst_rp[i][1]:
#                 # print(lst_ld[k], "c", i, k)

#             if lst_ld[i][1] < lst_rp[k][1] < lst_rp[i][1]:
#                 # print(lst_ld[k])
