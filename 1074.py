## n = 2
## 2 x 2


## n = 3
## 2^2 x 2^2

## n = 4
## 2^3 x 2^3

## 2^3를 알 때 우리는 무엇을 해야하는가를 생각했을 때
"""
생각해보면 각 행/열 수로 나눴을 때 4부분으로 나뉘어짐.
2x2를 생각해보면
    0 1
    - -
0 | 0 1
1 | 2 3
인데 왼쪽 위 -> 오른쪽 위 -> 왼쪽 아래 -> 오른쪽 아래

순으로 이동을 하게 됨

마찬가지로
4 x 4일 때도 크게만 본다면
     0   1  2  3
     -   -  -  -
0  |  0  1  4  5
1  |  2  3  6  7
2  |  8  9 12 13
3  | 10 11 14 15
인데
작은 왼쪽 위 -> 오른쪽 위 -> 왼쪽 아래 -> 오른쪽 아래
를 한번 진행하면 큰 오른쪽 아래로 이동함
그럼 이게 반복이 되어버림

행/열로 나뉘었을 때 각 범위를 추론할 수 있게됨.

"""
# r = 1 # 행
# c = 4 # 열
# n = 3

n, r, c = map(int, input().split())
lst = [2**i for i in range(n, -1, -1)]
start_idx = 0
for x in lst:
    row = r//x
    col = c//x

    if row == 0 and col == 1:
        start_idx += x**2 if x != 1  else 1
    elif row == 1 and col == 0:
        start_idx += x**2 * 2 if x != 1  else 2
    elif row == 1 and col == 1:
        start_idx += x**2 * 3 if x != 1  else 3

    r %= x
    c %= x

print(start_idx)