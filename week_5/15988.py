import sys
input = sys.stdin.readline

n = int(input())

d = [0] * (1000000+1)
d[0] = 1
d[1] = 2
d[2] = 4

for i in range(3, 1000001) :
    d[i] = (d[i-3] + d[i-2] + d[i-1]) % 1000000009

for _ in range(n):
    t = int(input())
    print(d[t+1])
