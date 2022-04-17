# try1 -> 성공
import sys
input = sys.stdin.readline

n = int(input())
MOD = 9901
# UPPER_RANGE = 100_000
dp = [[0,0,0] for _ in range(n+1)]

dp[1] = [1,1,1]
for i in range(2,n+1):
  dp[i][0] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%MOD
  dp[i][1] = (dp[i-1][0] + dp[i-1][2])%MOD
  dp[i][2] = (dp[i-1][0] + dp[i-1][1])%MOD

print(sum(dp[n])%MOD)