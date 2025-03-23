N = int(input())
# N = 1

def finddot(n):
    if n == 0:
        return 2
    else:
        return finddot(n-1) + 2**(n-1)
    
    
dot = finddot(N)
print(dot**2)