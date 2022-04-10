# 모범답안
import sys
input = sys.stdin.readline

n = int(input())
MAX_RANGE = 10_000
cost = [0]*(MAX_RANGE+1)
dp = [0]*(MAX_RANGE+1)

for i in range(1,n+1):
  cost[i] = int(input())


dp[1] = cost[1]
dp[2] = cost[1] + cost[2]
dp[3] = max(cost[3]+cost[2],cost[3]+cost[1],dp[2])

for i in range(4,n+1):

# i번째 잔을 마셨을 때의 최대 비용
# i-2,i-1,i
# max(OOX, OXO, XOO)
  dp[i] = max(dp[i-1],cost[i]+dp[i-2],cost[i]+cost[i-1]+dp[i-3])

print(max(dp))