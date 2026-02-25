import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

counts = {}

count = 1
start = 0
end = 0
# 범위가 start ~ end 사이에 있는걸로
while end < n:
    val = lst[end]
    counts[val] = counts.get(val, 0) + 1 # 탕후를 번호 : 번호 수
    while len(counts) >= 3: # 탕후루가 종류가 3개 이상일 때 반복
        out_val = lst[start]  # 가장 첫 자리를 1감소 (오른쪽으로 이동)
        counts[out_val] -= 1
        if counts[out_val] == 0:
            del counts[out_val] # 그때 이동했을 때 종류가 사라지면 dict에서 삭제
        start += 1

    if count <  end - start + 1:
        count = end - start + 1

    end += 1


print(count)




# while True:
#     if end == n+1:
#         break
#     sliced = lst[start:end]
#     if len(set(sliced)) >= 3:
#         start += 1
#         continue
#
#     end += 1
#     if count <  end - start -1:
#         count = end - start -1
#
# print(count)


"""

[1 1 2] 8 4

"""