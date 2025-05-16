s1, s2 = map(int, input().split())

set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))
print(len((set_1 - set_2) | (set_2 - set_1)))