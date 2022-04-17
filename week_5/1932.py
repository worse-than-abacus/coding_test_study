# try1 -> 성공
import sys
input = sys.stdin.readline

UPPER_RANGE = 500
n = int(input())
dp = [[0]*UPPER_RANGE for _ in range(UPPER_RANGE)]
cost = [[0]*UPPER_RANGE for _ in range(UPPER_RANGE)]


for i in range(n):
  cost_row = list(map(int,input().split()))
  cost[i] = cost_row + (n-i-1)*[0]

dp[0][0] = cost[0][0]
dp[1][0] = cost[0][0] + cost[1][0]
dp[1][1] = cost[0][0] + cost[1][1]

for row in range(n):
  for col in range(n):
      # row의 col 번째 수를 선택했을 때, 누적 합의 최대값
    dp[row][col] = max(dp[row-1][col-1],dp[row-1][col])+cost[row][col]

print(max(dp[n-1]))