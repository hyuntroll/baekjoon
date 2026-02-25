n = int(input())

def hanoi(r, start, end, step):
    if r == 1:
        print(f"{start} -> {end}")
    else:
        hanoi(r-1, start, step, end)
        print(f"{start} -> {end}")
        hanoi(r-1, step, end, start)

print(2**n -1)
if n <= 20:
    hanoi(n, 1, 3, 2)