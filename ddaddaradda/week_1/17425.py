# 시간초과
for _ in range(int(input())):
    sum = 0
    n = int(input())
    for i in range(1,n+1):
        sum += (n//i)*i
    print(sum)


#1
M=1000001
D=[1]*1000001
for i in range (2,M):
    j=1
    while i*j<=M-1:
        D[i*j] += i
        j +=1
S=[0]*M
for i in range (1,M):
    S[i] = S[i-1] + D[i]

for _ in range(int(input())):
    n=int(input())
    print(S[n])


#2
import sys

M=1000001
D=[1]*1000001
for i in range (2,M):
    j=1
    while i*j<=M-1:
        D[i*j] += i
        j +=1
S=[0]*M
for i in range (1,M):
    S[i] = S[i-1] + D[i]

for _ in range(int(input())):
    n=int(input())
    print(S[n])

n = int(input())
for _ in range(n):
    a = int(sys.stdin.readline())
    sys.stdout.write(str(S[a])+"\n")