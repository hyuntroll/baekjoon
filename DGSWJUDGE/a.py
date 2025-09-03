a_lst = 'ALT B1ND SAMDI Louter CNS MODI DUCAMI Chatty'.split()
b_lst = 'DROP InD 8BIT C0nnect draw Scheck DGSWFC Warriors cyclists'.split()


def check_club(lst):
    a_cnt = 0

    # 중복이 있는 경우에
    if len(lst) != len(set(lst)):
        return "NO"

    # 리스트 안에 없는 경우 동아리에 가입을 시도할 경우, + 창체 동아리 개수 추적
    for cl in lst:
        if cl not in a_lst and cl not in b_lst:
            return "NO"
        elif cl in a_lst:
            a_cnt += 1
    
    if a_cnt == 1:
        return "YES"
    else:
        return "NO"

for _ in range(int(input())):
    m = int(input())
    
    print(
        check_club(input().split())
    )

