N = int(input())

lst_ld = []
# lst_rp = []

for i in range(N):
    left, down = map(int, input().split())
    lst_ld.append((left, down))
    # lst_rp.append((left+10, down +10))
current_fuck = []

shit = len(lst_ld) * 100


def sets(n):
    for i in range(len(lst_ld)):
        test_lr(i)

def test_lr(n):
    global shit
    
    lr = False
    ub = False

    for i in range(len(lst_ld)):
        if i != n and ((i, n) not in current_fuck and (n, i) not in current_fuck) :
            
            if lst_ld[n][0] <= lst_ld[i][0] <= lst_ld[n][0] + 10:
                lr = lst_ld[n][0] + 10 - lst_ld[i][0]
                ub = test_ub(i, n)
                if ub == False:
                    continue
                
                


            elif lst_ld[n][0] <= lst_ld[i][0] +10 <= lst_ld[n][0] + 10:
                lr = lst_ld[i][0] + 10 - lst_ld[n][0]
                ub = test_ub(i, n)
                if ub == False:
                    continue

            else:
                continue
            
            # print(ub, lr, ub*lr)
            shit -= ub * lr
            current_fuck.append((i, n))
            
                

def test_ub(i, n):
    if lst_ld[n][1] <= lst_ld[i][1] <= lst_ld[n][1] + 10:   
        return lst_ld[n][1] + 10 - lst_ld[i][1]
    elif lst_ld[n][1] <= lst_ld[i][1] +10 <= lst_ld[n][1] + 10:
        return lst_ld[i][1] + 10 - lst_ld[n][1]
    
    return False
                
sets(N)
        
print(shit)


# for i in range(N):
#     for k in range(N):
#         if lst_ld[i][0] <= lst_ld[k][0] <= lst_rp[i][0]:
#             if lst_ld[i][1] <= lst_ld[k][1] <= lst_rp[i][1]:
#                 # print(lst_ld[k])
#             if lst_ld[i][1] <= lst_rp[k][1] <= lst_rp[i][1]:
#                 # print(lst_ld[k], "b", i, k)
#         if lst_ld[i][0] <= lst_rp[k][0] <= lst_rp[i][0]:
#             if lst_ld[i][1] <= lst_ld[k][1] <= lst_rp[i][1]:
#                 # print(lst_ld[k], "c", i, k)

#             if lst_ld[i][1] <= lst_rp[k][1] <= lst_rp[i][1]:
#                 # print(lst_ld[k])

N = int(input())

lst_rect = []
same_rect = []

rect_area = N * 100


for i in range(N):
    left, down = map(int, input().split())
    lst_rect.append((left, down))
    # lst_rp.append((left+10, down +10))
def find_i_in_n(i, n, L_R):
    if lst_rect[n][L_R] <= lst_rect[i][L_R] <= lst_rect[n][L_R] + 10:
        return lst_rect[n][L_R] + 10 - lst_rect[i][L_R]
    elif lst_rect[n][L_R] <= lst_rect[i][L_R] + 10 <= lst_rect[n][L_R] + 10:
        return lst_rect[i][L_R] + 10 - lst_rect[n][L_R]

    return False

l_r = 0
u_b = 0
for i in range(N):
    for k in range(N):
        if i != k and (i, k) not in same_rect and (k, i) not in same_rect:
            l_r = find_i_in_n(i, k, 0)
            u_b = find_i_in_n(i, k, 1)
            if l_r != False and u_b != False:
                same_rect.append((i,k))
                rect_area -= l_r * u_b
                # print(l_r * u_b, l_r, u_b,i,k)
print(rect_area)