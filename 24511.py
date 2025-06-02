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