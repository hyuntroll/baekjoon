N, M, b = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
mx = 0; mn = False
for l in lst:
    mx = max(mx, max(l))
    if mn == False:
        mn = min(l)
    else:
        mn = min(mn,min(l))

ans = 0
t = 0
# 다 부숴보던가
for i in range(N):
    for k in range(M):
        t += (lst[i][k] -mn) * 2
        b += lst[i][k] -mn
print(t, mn)


# 설치하고 부숴서 해보던가


row, col, block_count = map(int, input().split())
blocks = []
for _ in range(row):
    blocks.extend(list(map(int, input().split())))

clock = None

def check():
    f = blocks[0]
    for b in blocks:
        if f != b:
            return False
    return True

def bf(idx, temp_clock, bl_count):
    global block_count, clock
    if check():
        return True

    # 블럭 부수는 경우의 수
    if blocks[idx] > 0:
        blocks[idx] -= 1
        bl_count += 1
        temp_clock += 2

        for i in range(row*col):
            if idx != i and bf(i, temp_clock, bl_count):
                return True

        blocks[idx] += 1
        bl_count -= 1
        temp_clock -= 2

    # 블럭을 설치하는 경우의 수
    elif blocks[idx] < 256 and bl_count > 0:
        blocks[idx] += 1
        bl_count -= 1
        temp_clock += 1

        for i in range(row*col):
            if idx != i and bf(i, temp_clock, bl_count):
                return True

        blocks[idx] -= 1
        bl_count += 1
        temp_clock -= 1

    return False

bf(0, 0, block_count)