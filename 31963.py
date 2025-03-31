N = int(input())

nn = list(map(int, input().split()))

ans = 0 

for i in range(N):

    if i != N-1:

        while nn[i] > nn[i+1]:

            

            nn[i+1] = nn[i+1] << 1

            ans += 1


print(ans)