##  하나씩 해서 남은거는 그 남은거에서 하고 그거하고 또 남은거 


'''

1    1 2
2    2
3    3
     4



'''
dp = []

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    cnt = 0
    # for i in range(b-a+1):
    def f(cur, lim):
        global cnt
        if cur == 1:
            cnt += lim
            return lim
        
        for i in dp:
            if i[0] == cur and i[1] == lim:
                return i[2]
        else:
            things = 0
            for i in range(1, lim-cur+2):
                # print(i, cur, lim)
                things += f(cur-1, lim-i)
            dp.append([cur, lim, things])
            return things
            

    print(f(a, b))
    # print(cnt)