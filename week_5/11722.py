# try 2 j [0,i)
# try 1, j [1,i) 
import sys
input = sys.stdin.readline
n = int(input())
cost = list(map(int,input().split()))
dp = [1] * (n)


for i in range(n):
  for j in range(i):
    if dp[i] <= dp[j] and cost[i] < cost[j]:
      dp[i] = dp[j] + 1

print(max(dp))