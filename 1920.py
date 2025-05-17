n = int(input())
dit = {k: 1 for k in list(map(int, input().split()))}
m = int(input())
print(   *[  1 if dit.get(i) else 0 for i in list(map(int, input().split()))  ] , sep="\n" )