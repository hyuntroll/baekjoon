"""
첫 번째 줄에 좋아하는 문자열 의 길이  서로 다른 문자의 개수  연속된 길이 이 공백으로 구분되어 주어진다
두 번째 줄에 문자열 가 주어진다 는 영어 소문자로만 이루어진 문자열이다
출력
조건을 만족하는 비밀번호의 개수를 정수로 출력한다

"""
import sys; input=sys.stdin.readline
import deque
n, k, l = map(int, input().split())
string = input()
cnt = 0
loop = n - l + 1
queue = deque()
# 문자열 슬라이싱 말고 큐에 넣어서 오래된거 빼고, 새로운거 집어넣는데 집어넣은거 카운트만 생각하면 될듯
for idx in range(loop):
    cur_str = string[idx:idx+l]

    if len(set(cur_str)) <= k:
        cnt += 1
print(cnt)