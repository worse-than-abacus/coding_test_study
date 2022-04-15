n,k =  map(int,input().split())

dp=[1]*(n+1)
for i in range(1,k):
  temp_dp=[0]*(n+1)
  for j in range(n+1):
    temp_dp[j]=sum(dp[0:j+1])
  for j in range(n+1):
    dp[j] = temp_dp[j]

print(dp[n]%1_000_000_000)