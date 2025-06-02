'''
queuestack

queue 1
stack 2
stack 3
queue 4

input = 2, 4, 7


1st
2

queue 1 2 return 1
stack 2 1 return 1
stack 3 1 return 1
queue 4 1 return 4

2nd
4

queue 2 4 return 2
stack 2 2 return 2
stack 3 2 return 2
queue 1 2 return 1

3rd
7

queue 4 7 return 4
stack 2 4 return 4
stack 3 4 return 4
queue 2 4 return 2


q 11
s
q 13
s
q 15
s

21 22 23 24 25 26

15
13
11
21 -
22 -
23 -

보면 스택은 후입선출이기 때문에 그냥 흘려보내면 됨
그렇다면 큐일때만 생각하면 되는데
지금 저때를 보면 먼저 있던것들이 먼저 빠져나가니까 [ 11, 13, 15 ]
이게 하나씩 밀려나서 [ 21, 11, 13] -> pop 15
이런식으로 반복됨

그럼 우리는 뭘 해줘야 하냐
큐인것들 뽑아서 프린트 하고

그다음에도 남았다면 입력했던거 출력하면 됨


6
0 1 0 1 0 1
11 12 13 14 15 16
6
21 22 23 24 25 26
15 13 11 21 22 23 

'''
import sys;input=sys.stdin.readline
# from collections import list
qst = int(input())
l1 = list(map(int, input().split()))

l2 = list(map(int, input().split()))

l3 = list([i for i in range(qst) if not l1[i]])
# l3 = list(l2[i] for i in range(qst) if not l1[i])
# print(l3)
n = int(input())
lst = list(map(int, input().split()))
if n < len(l3):
    for i in range(n):
        print(l2[l3[-(i+1)]],end=" ")
else:
    for i in reversed(l3):
        print(l2[i], end=" ")
    for i in range(n - len(l3)):
        print(lst[i], end=" ")