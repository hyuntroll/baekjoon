import sys
input = sys.stdin.readline


ans = 0
count = int(input())
inlst = [0] + list(map(int, input().split()))

already_sum = {}

temp = 0
sum_list = []
for i in range(count+1):
    temp += inlst[i]
    sum_list.append(temp)
    
for k in range(3, count):
    for j in range(2, k):
        for i in range(1, j):
            case_a = sum_list[i]
            case_b = sum_list[j] - sum_list[i]
            case_c = sum_list[k] - sum_list[j]
            case_d = sum_list[-1] - sum_list[k]
            if (case_a) == (case_b) == (case_c) == (case_d):
                ans += 1
            

print(ans)