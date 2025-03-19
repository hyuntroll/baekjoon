N, k = map(int, input().split())

money_type = []
for i in range(N):
    money_type.append(int(input()))

money_type.sort(reverse=True)

def findcount(current_money):
    ans = 0
    for value in money_type:
        if value <= current_money:
            ans += current_money // value  
            current_money = current_money % value 

        if current_money == 0:
            break

    return ans

print(findcount(k))
