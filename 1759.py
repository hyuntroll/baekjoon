l, c = map(int, input().split())
mo = ['a', 'e', 'i', 'o', 'u']
lst = sorted(input().split())
visited = [False] * c
current_str = [None] * l

def bf(idx, max_len, count, latest_word_len):
    if idx == max_len:
        mo_c = 0
        for s in current_str:
            if s in mo:
                mo_c += 1
        if max_len - mo_c >= 2 and mo_c >= 1:
            print(*current_str, sep='')

        return

    for i in range(0, count):
        if not visited[i]:
            word_len = ord(lst[i])
            if latest_word_len > word_len:
                continue
            visited[i] = True
            current_str[idx] = lst[i]
            bf(idx+1, max_len, count, word_len)
            visited[i] = False

bf(0, l, c, 0)
