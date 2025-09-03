def newdash(current_i, idx): ## 작개 나누는 단계, 그 중 idx
            if current_i == 3:
                if idx == 2:
                    print(" ", end="")
                else:
                    print("-", end="")
            else:
                if idx == 2:
                    print(" "*(current_i//3), end="")
                    return

                for i in range(1, 3+1):
                    newdash(current_i//3, i)

while True:
    try:
        n = 3**int(input())

        ### 작개작개 나누기 그리고 나눈거를 다 만들면 위로 올라오기
        
                # pass

        ## for문을 좀 다르게 해서 cur_i가 들어왔을 때 이에맞게 for문을 돌리는 게 더 좋을 거 같은데요..?
        ## 돌리는 와중에 중간이라면 공백 하시고 ( 공백할 때는 cur_i 만큼 )
        # n = 81
        if n == 1:
            print("-", end="")
        else:
            for i in range(1, 3+1):
                newdash(n, i)
        print()
    except:
        break
    