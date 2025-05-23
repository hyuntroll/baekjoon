'''
a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.

아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 
단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.'''

''''
0층 
    1호
    2호
    3호
    4호
    5호
    6호 ---

a층 b호 n k
1층 7호라면
1+2+3+4+5+6+7


'''
lst = []

def find(a, b, i):
    global lst
    if i == a:
        return
    else:
        l = []
        for k in range(b):
            l.append(sum(lst[i][0:k+1]))
        lst.append(l)
        find(a, b, i+1)

n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    lst = [ list(range(1, b+1)) ] 
    find(a, b, 0)
    print(lst[-1][-1])
    
'''

a  b호의 사는 사람 수



0층

1 2 3 4 5 6 -- b

1층 b호
1층 
1 + 2 + 3 -- + b

'''