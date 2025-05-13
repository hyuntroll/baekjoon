N = int(input())
nlst = list(map(int, input().split()))
M = int(input())

def test(x):
    global nlst
    return int(x in nlst)

mlst = map(test, input().split())
print(list(mlst))
