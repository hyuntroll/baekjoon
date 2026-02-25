import sys
input = sys.stdin.readline

row, col, block_count = map(int, input().split())
blocks = []
for _ in range(row):
    blocks.extend(list(map(int, input().split())))

clock=float('inf')
height=-1
for h in range(min(blocks), max(blocks)+1):
    temp_clock = 0
    temp_count = block_count

    for block in blocks:
        if block > h: # 0 129
            temp_count += block - h # 130
            temp_clock += 2 * (block - h)
        elif block < h: #0 129
            temp_count -= h - block # 1
            temp_clock += h - block

    if temp_count < 0:
        continue

    if clock > temp_clock or (clock == temp_clock and height < h):
        height = h
        clock = temp_clock

print(clock, height)