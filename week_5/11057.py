n = int(input())
dp = [[1,1,1,1,1,1,1,1,1,1] for _ in range(n+1)]

for i in range(1,n):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])%10_007

print(sum(dp[n-1])%10_007)