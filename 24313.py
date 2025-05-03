'''
O(g(n)) = f(n) | 모든 n>=n0 에 대해 f(n) <=  c * g(n) 인 양의 상수 c 와 n0가 존재 } 

f(n) = a1n + a0 
양의 정수 c n0가 주어짐

-----

a1 = 7, a0 = 7,
c = 8, n0 = 1

f(n) = 7n + 7


7n + 7 | 모든 n>= 1에 대해 7n+7 <= 8n
 7 <= n


 
 이거 개어려움
'''


a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

n = n0

fn = a1 * n + a0
print(int(fn <= c * n and a1 <= c))



