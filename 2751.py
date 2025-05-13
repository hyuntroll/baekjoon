unsorted_lst = list(map(int, input().split()))


# 정렬 시에 왼, 오 index해두고 비교하면서 된거는 +1씩 아니면 나두기

def divid_lst(lst):
    if len(lst) <= 1:
        return lst
    
    center = len(lst)//2
    left = lst[:center]
    right = lst[center:]

    left_ = divid_lst(left)
    right_ = divid_lst(right)
    

def merge(left, right):
    
