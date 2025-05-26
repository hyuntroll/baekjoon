# unsorted_lst = list(map(int, input().split()))


# # 정렬 시에 왼, 오 index해두고 비교하면서 된거는 +1씩 아니면 나두기

# def divid_lst(lst):
#     if len(lst) <= 1:
#         return lst
    
#     center = len(lst)//2
#     left = lst[:center]
#     right = lst[center:]

#     left_ = divid_lst(left)
#     right_ = divid_lst(right)
    

# def merge(left, right):
# import sys; input = sys.stdin.readline

# # 삽입 정렬
# lst = [int(input()) for _ in range(int(input()))]

# for i in range(len(lst)-1):
#     min_idx = i
#     for j in range(i+1, len(lst)):
#         if lst[min_idx] > lst[j]:
#             min_idx = j

#     lst[min_idx], lst[i] = lst[i], lst[min_idx]
# print(*lst, sep="\n")


# 파이썬에서는 기본 정렬이 빨랐구요~
import sys; input = sys.stdin.readline

print(*sorted([int(input()) for _ in range(int(input()))]), sep="\n")