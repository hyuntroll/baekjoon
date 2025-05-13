cur = 0
score = 0



N = int(input())
for i in range(N):
    cur = 0
    score = 0
    s = input()
    for k in s:
        if "O" == k:
            cur +=1
            
        else:
            cur = 0
        score += cur
    print(score)
