# lst = []
# count_lst = [0] * 10001
# for i in range(int(input())):
#     lst.append(int(input()))
#     # 각 원소의 개수를 
#     count_lst[i] += 1
# result = [0] * len(lst)
# for i in lst:
#     count_lst[i] += 1

# # idx 0 1 2 3 4 5 6 7 8 9
# # val 0 1 1 2 2 1 0 1 0 1

# # 누적합 계산
# for i in range(1, len(count_lst)):
#     count_lst[i] += count_lst[i-1]

# # idx 0 1 2 3 4 5 6 7 8 9
# # val 0 1 2 4 6 7 7 8 0 9

# '''
# 이때 원래 lst에 있는 값을 result에 본인의 index란에 넣으면 됨
# 왜냐하면 그 앞에 있는 값들이 몇개 있는지가 val에 적혀있기 때문| 그리고 본인은 
# 누적합에서 -1 해줘야지 다음 값이 들어왔을 때 그 앞에 정렬되기 때문

# '''

# for i in lst:
#     idx = count_lst[i]
#     result[idx-1] = i
#     count_lst[i] -= 1

# print(result)

import sys

input = sys.stdin.readline

count_lst = [0] * 10001

for _ in range(int(input())):
    num = int(input())
    count_lst[num] +=1

for i in range(10001):
    if count_lst[i] > 0:
        for j in range(count_lst[i]):
            print(i)