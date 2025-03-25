N = int(input())

interesting_x_y = []

for i in range(N):
    left, down = map(int, input().split())
    for i in range(left, left+10):
        for k in range(down, down+10):
            interesting_x_y.append((i, k)) #10 x 10 정사각형을 하나의 좌표로 1x1모양의 정사각형으로 모두 나타냄
            # 1 1을 입력하면 (1, 1) (1, 2) (1, 3)... (1, 10) (2, 1) .... (10, 10) 이런식으로 한칸한칸을 모두 리스트에 저장
print(len(set(interesting_x_y))) # 이중에서 좌표가 겹치는 부분을 교집합으로 합쳐줌 그리고 그 결과를 출력함