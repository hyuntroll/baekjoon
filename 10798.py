lst = []
max_len = 0
for i in range(5):
    lst.append(input().replace(' ', ''))
    max_len = max(max_len, len(lst[i]))



for i in range(max_len):
    for k in range(5):
        try:
            print(lst[k][i], end="")
        except:
            pass
print()