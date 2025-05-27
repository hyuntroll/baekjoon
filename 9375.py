for _ in range(int(input())):
    n = int(input())
    wearing = {}
    for _ in range(n):
        new = input().split()[1]
        if new not in wearing:
            wearing[new] =1
        else:
            wearing[new] +=1
        
    tree = 1
    for k in wearing:
        tree *= wearing[k]+1
    print(tree-1)