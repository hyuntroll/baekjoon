import sys; input=sys.stdin.readline

com = int(input())
com_s = int(input())


link_d = {}
vir = {i: False for i in range(1, com+1)}

for i in range(com_s):
    k, v = map(int, input().split())
    if k not in link_d:
        link_d[k] = [ v ]
    else:
        link_d[k].append(v)



def findVir(key):
    global link_d, vir
    if not vir[key]: ## 감염된 컴퓨터와 연결되어있는거 찾기 ( 감염된 컴퓨터가 키의 리스트로 연결 되었을 때 그 키가 감염되었음을 알림)
        vir[key] = True
        for k, value in link_d.items():
            if key in value:
                findVir(k)

        if key in link_d: ## 감염된 컴퓨터와 연결되어있는거 찾기 ( 감염된 컴퓨터가 키로 연결되어 있는경우)
            for k in link_d[key]:
                findVir(k)
findVir(1)
# print(vir)

print(len([k for k in vir if vir[k]]) -1)

# print(link_d)
