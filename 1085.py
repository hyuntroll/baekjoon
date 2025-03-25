need_dot = [0, 0]
x_l = []
y_l = []
for i in range(3):
    x, y = map(int, input().split())
    x_l.append(x); y_l.append(y)

set_pos = [list(set(x_l)), list(set(y_l))]

if x_l.count(x_l[0]) == 2:
    set_pos[0].remove(x_l[0])
    need_dot[0] = set_pos[0][0]
else:
    need_dot[0] = x_l[0]
if y_l.count(y_l[0]) == 2:
    set_pos[1].remove(y_l[0])
    need_dot[1] = set_pos[1][0]
else:
    need_dot[1] = y_l[0]

print(*need_dot)

####