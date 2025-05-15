'''
좌표가 주어지고 좌표에 압축을 적용하는 문제
Xi 를 압축했을 때 X'i의 값은 Xi > Xj 에서 서로 다른 Xj 의 개수
이때 X'1 .. X'2 ------ X'N을 출력하는 문제



'''
import sys
input = sys.stdin.readline

n = int(input())

x_pos = list(map(int, input().split()))

'''모든 수를 0이상으로 만들어주기'''
# x_pos = [i - min(x_pos) for i in x_pos]
# print(x_pos)

# 같은거 지우고 정렬해서 key value형태로
x_key = {}
x_lst = sorted(set(x_pos))
for i in range(len(x_lst)):
    x_key[x_lst[i]] = i

# x_zip = dict(enumerate(sorted(list(set(x_pos)))), )
for i in x_pos:
    print(x_key[i], sep=" ")