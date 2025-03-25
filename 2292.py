# n = int(input())

# cnt = n
# ans = 0



# while cnt != 1:
#     pass



current = 1
for i in range(2, 10):
# i = 2
    hex = 6*(i-2) + 6
    current += hex
    print(hex, f"{current-hex+1}~{current}")


'''
벌집수 숫자 크기
6 2~7 hex = 2
12 8~19 hex = 3
18 20~37 hex = 4 .....
24 38~61
30 62~91
36 92~127
42 128~169
48 170~217
'''

n = int(input())
str_end = [1, 1] # 육각형을 이루는 벌집에 적힌 숫자의 시작값과 끝값 크기가 1일대는 1, 1
# 2일때는 2 ~ 7 까진데 첫값은 그전 끝값에서 1을 더하고 
# 끝값은 현재 벌집크기 에서 1을 뺀 다음 6을 곱하면 된다.
# 최단값은  벌집 크기와 같기때문에 벌집 크기를 구하면 됨


current_hex = 1
while not(str_end[0] <= n <= str_end[1]):
    current_hex += 1
    str_end[0] = str_end[1] +1; str_end[1] += (current_hex-1)*6 
    print(str_end)
print(current_hex)

###########
count = 1
while 1 < n:
    n -= count*6  # 시작값은 6씩 커지니까 값이 n이 -가 나오거나 1이 될 때 빠져나오면 바로 구할 수 있다. 
    # 벌집 수는 6의 배수이고 시작숫자는 1이다. 그렇기에 6의 배수씩 뺐을 때 1 < n이 나오면 된다. 이동한 칸은 벌집 크기와 같기 때문에
    count += 1
print(count)