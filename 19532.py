a, b, c, d, e, f = map(int, input().split())

print((c*e - b*f)//(a*e-d*b), (c*d-f*a)//(b*d-e*a))



for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)