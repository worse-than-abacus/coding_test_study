# try 4 -> 성공
# import pprint
# try 1 ~ 3
# % MOD로 안나누어서 틀림
n = int(input())
MOD =  1_000_000_000
# i번째 자리수 , [0,9]
dp = [[0 for _ in range(0,9+1)] for _ in range(n+1)]
for num in range(1,9+1):
  dp[1][num] = 1
  
for i in range(2,n+1):
  for num in range(9+1):
    if num == 0:
      dp[i][num] = dp[i-1][1]
    elif num == 9:
      dp[i][num] = dp[i-1][8]
    else:
      dp[i][num] = dp[i-1][num-1] + dp[i-1][num+1]


# pprint.pprint(dp)

print(sum(dp[n])%MOD)      