A = [5, 9, 3, 6, 9, 5, 2, 10, 1]
B = [0] * (max(A)+1)
C = [0] * len(A)
for i in A:
    B[i] += 1
for i in range(1, len(B)):
    B[i] = B[i] + B[i-1]
for i in range(0, len(A)):
    C[B[A[i]]-1 ] = A[i]


print(C)