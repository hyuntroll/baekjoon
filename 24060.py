n, k = map(int, input().split())
lst = list(map(int, input().split()))


memory = []
def merge_sort(arr):
    global memory
    if len(arr) < 2:
        return arr
    
    mid = len(arr)//2
    
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = 0
    r = 0

    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] >= right_arr[r]:
            merged_arr.append(right_arr[r])
            memory.append(right_arr[r])
            r += 1
        else:
            merged_arr.append(left_arr[l])
            memory.append(left_arr[l])

            l += 1
    
    while r < len(right_arr):
        memory.append(right_arr[r])
        merged_arr.append(right_arr[r])
        r += 1
    while l < len(left_arr):
        merged_arr.append(left_arr[l])
        memory.append(left_arr[l])

        l += 1
    
    return merged_arr

# print(merge_sort(lst))
print(memory.pop(k) if len(memory) > k else -1)