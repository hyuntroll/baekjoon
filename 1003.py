import sys; input=sys.stdin.readline

zl = [0] * 41
ol = [0] * 41
zl[0] = 1; zl[1] = 0
ol[0] = 0; ol[1] = 1

for i in range(2, 41):
    zl[i] = zl[i-1] + zl[i-2]
    ol[i] = ol[i-1] + ol[i-2]

for _ in range(int(input())):
    n = int(input())
    print(zl[n], ol[n])

# zero랑 one이 몇번 출력되는지만 구해서 | 값에 맞는 0, 1 개수를 출력한다 -> 더하면 값이 나옴 ㅇㅇ