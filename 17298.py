n = int(input())
lst = list(map(int, input().split()))
NGE = [-1] * n
stack = []
for i in range(n):

    while stack and lst[stack[-1]] < lst[i]:
        # print(stack)
        NGE[stack.pop()] = lst[i]

    stack.append(i)
print(*NGE)

# 스택에 관한 중요한 문제 문제 풀이할 가치가 있을 듯

'''
i = 0
stack = [] -> [0]
i = 1
stack = [0]
lst[stack[-1]] < lst[i]


3 2 8 4 0 8 9 4 2


'''