string = input().upper()

diction = {}
max_ch_n = 0
max_ch = '?'
for i in string:
    if i in diction:
        continue
    diction[i] = string.count(i)

# print(diction)

test = list(diction.values())

if test.count(max(test)) > 1:
    print("?")
else:
    print(list(diction.keys())[test.index(max(test))])