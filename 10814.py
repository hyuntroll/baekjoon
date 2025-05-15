# dit = {}
# n = int(input())
# for _ in range(n):
#     value, key = input().split()
#     dit[key] = int(value)

# # for key in sorted(dit.keys(), key=lambda x: dit[x]):
#     # print(dit[key], key, sep=" ")


# dit_lst = list(dit.keys())


# for i in range(n):
#     for j in range(1, n-i):
#         if dit[dit_lst[j-1]] > dit[dit_lst[j]]:
#             dit_lst[j-1], dit_lst[j] = dit_lst[j], dit_lst[j-1]

# for i in dit_lst:
#     print(dit[i], i, sep=" ")


# # 버블 정렬


lst = []
n = int(input())
for _ in range(n):
    a, b = input().split()
    lst.append((int(a), b))

lst.sort(key=lambda x: x[0])

# for i in range(n):
#     for j in range(1, n-i):
#         if lst[j-1][0] > lst[j][0]:
#             lst[j-1], lst[j] = lst[j], lst[j-1]

for i in range(n):
    print(lst[i][0], lst[i][1], sep=" ")