import sys; input = sys.stdin.readline

for i in range(int(input())):
    
    n = int(input())

    def fact(n):
        f = 1
        for i in range(1, n+1):
            f *= i
        return f

    """
    먼저 3을 최대한 사용할 수 있는 개수
    """
    three = n//3
    cnt = 0

    for t in range(three+1):
        "이때 2를 최대한 사용할 수 있는 개수"
        two = (n-t*3)//2
        for w in range(two+1):
            one = (n-t*3-w*2)
            cnt += fact(t +w +one)//(fact(t)*fact(w)*fact(one))

    print(cnt)
