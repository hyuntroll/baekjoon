## https://school.programmers.co.kr/learn/courses/30/lessons/389478

def solution(n, w, num):
    n_floor = n
    number = num
    answer = 0
    
    ans_w = 0 # 몇 층인지
    ans_num = 0 # 몇 번째 칸에 있는지
    
    while n_floor >= 1:
        ans_w += 1
        n_floor -= w
    while number >= 1:
        ans_num += 1
        number -= w
    
    answer = ans_w - ans_num + 1
    # print(answer)


    if (ans_num%2 != 0 and ans_w % 2 == 0) or (ans_num%2 == 0 and ans_w % 2 != 0):
        # print("d")
        if ans_w * w - n >= num - (ans_num-1) * w:
            answer -= 1
    else:
        # print("f", ans_w * w - n)
        if ans_w * w - n >=  ans_num * w - num + 1:
            answer -= 1
    
    return answer

print(solution(13, 3, 6))