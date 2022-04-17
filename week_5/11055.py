# try 2 -> 성공
# try 1에서  if dp[i] <= dp[j] 빠뜨림
import sys

input = sys.stdin.readline
UPPER_RANGE = 1_000
n = int(input())
dp = [0]*n
cost = list(map(int,input().split()))

answer = -999

for i in range(0,n):
  for j in range(i):
    if dp[i] <= dp[j] and cost[i] > cost[j]:
      dp[i] = dp[j]
    
  dp[i] += cost[i]
  answer= max(answer,dp[i])    

print(answer)