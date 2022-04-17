# try 1 -> 성공

import sys

input = sys.stdin.readline

MOD = 1_000_000_009
UPPER_RANGE = 1_000_000

dp = [0] * (UPPER_RANGE+1)
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,UPPER_RANGE+1):
  dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

T = int(input())
for _ in range(T):
  n = int(input())
  print(dp[n])