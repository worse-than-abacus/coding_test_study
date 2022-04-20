# try 1 -> 성공
import sys
input = sys.stdin.readline

n = int(input())
cost = list(map(int,input().split()))
dp = [1]*(1000+1)
for i in range(n):
  for j in range(i):
    if dp[i] <= dp[j] and cost[i]>cost[j]:
      dp[i] = dp[j] + 1

print(max(dp))