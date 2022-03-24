# try1 시간초과
n=int(input())
ans=''
for i in range(1,n+1):
  ans += str(i)
print(len(ans))

#try
n = str(input())
ans =0
if len(n) == 1 : 
    ans = n
else :
    for i in range(len(n)):
        if i+1 == len(n):
            ans += ((int(n))-10**i+1)*(i+1) ## 이부분 틀렸었음
        else :
            ans += (i+1)*9*10**i
print(ans)

## 딕셔너리 풀이
import sys

input = sys.stdin.readline
N = int(input())
n = len(str(N)) 

ndigit = {i:9*10**(i-1) for i in range(1,8+1)}
answer = 0


for i in range(1, n):
  answer += i*ndigit[i]
answer += n * (N-10**(n-1)+1) 
print(answer)