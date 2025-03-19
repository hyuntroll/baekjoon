string = input()

count = 0

for i in range(len(string)):
    if (string[i] != string[len(string)-1-i]):
        print(0)
        break
else:
    print(1)