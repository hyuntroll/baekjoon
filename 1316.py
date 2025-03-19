
n = int(input())

ans = 0
for i in range(n):
    test = input()
    test_lst = []

    current_chr = test[0]
    test_lst.append(test[0])

    for i in test:
        if i != current_chr:
            if i in test_lst:
                break
            current_chr = i
            test_lst.append(i)
    else:
        # print("wow")
        # print("니얼굴", test)
        ans += 1

print(ans)