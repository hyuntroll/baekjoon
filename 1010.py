##  하나씩 해서 남은거는 그 남은거에서 하고 그거하고 또 남은거 
## 1010 다리 하나씩 두면서 첫번째 다리에서 몇개까지 놓을 수 있는지 해서
## 두번째 다리는 거기서 ㄷ'ㅗ 몇개 둘수 있는지 ----
## 마지막 다리에서는 남은 위치 수 구해서 리턴
## 그래서 n번재 다리에서 몇개가 남았을 때 몇개의 경우의 수가 나오는지 리스트로 저장
## 재귀할 때 리스트 안에 있으면 그 값 바로 리턴

## 


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