# 모범답안
import sys
input = sys.stdin.readline

n = int(input())
dp = [[0,0,0]]
for i in range(n):
  dp.append(list(map(int,input().strip().split())))

# i번째 집의 최소 비용
for i in range(1,n+1):
  # i번째 집을 빨간색으로 칠했을 때 최소 비용
  dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + dp[i][0]
  # i번째 집을 초록색으로 칠했을 때 최소 비용
  dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + dp[i][1]
  # i번째 집을 파란색으로 칠했을 때 최소 비용
  dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + dp[i][2]
print(min(dp[i]))