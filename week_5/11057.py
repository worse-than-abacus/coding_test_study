# try 3 -> 성공
# 1,2에서 최종 답 % MOD 빠뜨림
import sys
input = sys.stdin.readline

n = int(input())
MOD = 10_007
dp = [[0] * 10 for _ in range(n+1)]

dp[1] = [1]*10
for row in range(2,n+1):
  for num in range(10):
    for cal_num in range(num+1):
      dp[row][num] += dp[row-1][cal_num]
    dp[row][num] %= MOD

print(sum(dp[n])%MOD)
