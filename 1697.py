from collections import deque
s, k = map(int, input().split())


def shut(su, br):
    q = deque()
    q.append((su, 0))
    visited={su}

    while True:
        pos, time = q.popleft()
        if pos == br:
            return time

        if  0 <= pos+1 <= 100000 and pos +1 not in visited:
            q.append((pos+1, time+1))
            visited.add(pos+1)
        if  0 <= pos-1 <= 100000 and pos -1 not in visited:
            q.append((pos-1, time+1))
            visited.add(pos - 1)
        if  0 <= pos*2 <= 100000 and pos *2 not in visited:
            q.append((2*pos, time+1))
            visited.add(pos *2)


print(shut(s, k))