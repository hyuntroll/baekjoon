N = int(input())

# N = 21
row = []
col = []
n_1 = 0
n_2 = 1


def find(n):
    global n_1
    global n_2
    if n == 1:
        return (1, 1)
    

    
    # n_2 = 1
    row.append(1)
    col.append(1)
    
    while True:

        col.append(col[-1] +1)
        # col.append(n_1)
        n_1 += 1
        col.append(col[-1] + 4*n_1)

        row.append(row[-1] + 2*n_2)
        row.append(row[-1] + 1)
        n_2 += 2
        # print(row, col)

        if n_1 % 2 != 0:
            if col[n_1] <= n <= row[n_1]:
                return (col[n_1], row[n_1])
        else:
            if row[n_1] <= n <= col[n_1]:
                return (row[n_1], col[n_1])

interest = find(N)
# print(interest, n_1)
a = 1
b = 1

if n_1 % 2 == 0:
    a = n_1 +1
    if interest[0] <= N:
        for i in range(interest[0], N):
            a -= 1
            b += 1
    else:
        for i in range(N, interest[1]):
            a -= 1
            b += 1
        
else:
    b = n_1 + 1
    if interest[0] <= N:
        for i in range(interest[0], N):
            a += 1
            b -= 1
    else:
        for i in range(N, interest[1]):
            a += 1
            b -= 1

print(f"{a}/{b}")


