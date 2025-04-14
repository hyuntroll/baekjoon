list_length = list(map(int, input().split()))

max_len = max(list_length)
list_length.remove(max_len)

while sum(list_length) <= max_len:
    max_len -= 1

print(sum(list_length) + max_len)