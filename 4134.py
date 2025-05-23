def gcd(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    i = int(input())
    while not gcd(i) or i <= 1: i+=1
    print(i)