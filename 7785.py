n = int(input())

eum = {}

for i in range(n):
    key, value = input().split()
    eum[key] = value
for key, value in sorted(eum.items(), reverse=True):
    if value == "enter":
        print(key)


