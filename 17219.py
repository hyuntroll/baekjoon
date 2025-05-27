n, m = map(int, input().split())
site = {}
for _ in range(n):
    key, value = input().split()
    site[key] = value
for _ in range(m):
    print(site[input()])