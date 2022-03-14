
import sys
input = sys.stdin.readline
a,b = map(int,input().split())

def gcd(a,b):
    while b:
# a < b이면 a = b, b = a%b = a 이므로 순서 자동 정렬
# 두 서로소인 정수 A, B
# a,b의 최대공약수 G , a = GA, b = GB
# a = b*q + r
# G*A = G*B*q + r
# r = G*(A-B*q)
# 따라서, b와 r의 최대공약수 G = a와 b의 최대공약수 G
# 이때 a%b == 0이면 stop a = m*b 배수관계이므로 최대공약수는 m
# gcd(a,b) = gcd(b,r) = ... 이므로  G = m
        a, b = b, a % b
        print(a, b)
    return a

print(gcd(a, b))

# a*b = A*B*G*G
# a*b/G = A*B*G, 최대공배수
print(a * b // gcd(a, b))