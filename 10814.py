dit = {}
n = int(input())
for _ in range(n):
    key, value = input().split()
    dit[value] = int(key)

for value in sorted(dit.keys(), key=lambda x: dit[x]):
    print(dit[value], value, sep=" ")
# dit_lst = list(dit.keys())


# for i in range(n):
#     for j in range(1, n -i):
#         if dit[dit_lst[j-1]] > dit[dit_lst[j]]:
#             dit_lst[j-1], dit_lst[j] = dit_lst[j], dit_lst[j-1]

# for i in dit_lst:
#     print(dit[i], i, sep=" ")


# 버블 정렬