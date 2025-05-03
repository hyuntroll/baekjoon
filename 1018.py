'''

처음이 BW로 시작하면
그다음 WBWB 이런식으로 되겠죠

처음 행 열 인덱스 걍 다 파악해서 색 바꾸는거 저장하죠;

바꾸는 경우는 언제로 정해야 하는거지
배열 상 안맞으면 다 바꿔야 할텐데

하나는 시작을 B로 하고
하나는 시작을 W로 생각해서 슬라이싱 한것 중 다른게 있으면 B나 W로 교체
그 교체 횟수를 저장 하고 최솟값

x%2 == q 
q가 0 일 땐 처음이 B
1 일 땐 처음이 W

if q == 0:
    t = "B"
    else
    t = "W"
if x%2 == q:

        

'''



n, m = map(int, input().split())
lst = []
ans = []
cur = ''
for i in range(n):
    lst.append(input())

# print("\n")

for i in range(0, n-8+1):
    for k in range(0, m-8+1):
        for q in range(0, 2):
            te = "B" if q else "W"
            an = 0
            count = 0
            for j in range(i, i+8):   
                for p in lst[j][k:k+8]:
                    if j % 2 == 0:
                        if count % 2 == 0:
                            if te != p:
                                an +=1
                        else:
                            if te == p:
                                an += 1
                    else:
                        if count % 2 != 0:
                            if te != p:
                                an +=1
                        else:
                            if te == p:
                                an += 1
                    # print(p, end="")
                    count += 1
                # print()
            ans.append(an)
        # print()

print(min(ans))



n, m = map(int, input().split())
lst = []
word = "BWBWBWBWBW" # word[q+k+p//2]에서 k=1이고 p//2=1일때 word[9]까지 보니까 끝에 BW 추가
for _ in range(n):
    lst.append(input())

total = 64 #최솟값(64보다 큰 수가 나올수 없으므로 비교를 위해 64로 저장)
for i in range(n-7): #가로 반복 개수
    for j in range(m-7): #세로 반복 개수
        for k in range(2): #시작이 B인 경우와 W인 경우 2가지
            s = 0 #개수 합 초기화
            for p in range(8): #i, j로 정해진 시작점에서 p만큼 아래로, q만큼 오른쪽으로 간 문자
                for q in range(8):
                    if word[q+k+p%2] != lst[i+p][j+q]: #몰라 대충 맞겠지
                        s += 1
            if s < total:
                total = s

print(total)