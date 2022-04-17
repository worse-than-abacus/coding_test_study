# try 4
n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3,1001):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)

# dp 이해
# https://assb.tistory.com/entry/%EB%B0%B1%EC%A4%80-11726%EB%B2%88-2xn-%ED%83%80%EC%9D%BC%EB%A7%81
import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
# n = 1일때, 2가 존재하지 않음
# index 에러
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2])%10007

# 계산 과정 도중 나누지 않으면, MAX inteager 값을 넘어가서 에러 발생할 수도 있음
print(dp[n])

# try 1
import sys

input = sys.stdin.readline

n = int(input())

distance = [2] * (n+1)
distance[1] = 1

for i in range(2, n+1):
  
  distance[i] = distance[i-1]*2 +1


print(distance[n]%10007)