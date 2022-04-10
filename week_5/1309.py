# try1 메모리 초과
n= int(input())
dp = [[1,1,1] for _ in range(n)]

for i in range(1,n):
  dp[i][0] = sum(dp[i-1])
  dp[i][1] = dp[i-1][0] + dp[i-1][2]
  dp[i][2] = dp[i-1][0] + dp[i-1][1]

print(sum(dp[n-1]))

# try2 수학적 접근
n= int(input())
dp = [[1,2] for _ in range(n)]

for i in range(1,n):
  dp[i][0] = (dp[i-1][0] + dp[i-1][1])%9901
  dp[i][1] =  2*(dp[i-1][1]/2+ dp[i-1][0])%9901

print(int(sum(dp[n-1])%9901))

# try3 try1 수정
n= int(input())
dp = [[1,1,1] for _ in range(n)]

for i in range(1,n):
  dp[i][0] = sum(dp[i-1])%9901
  dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
  dp[i][2] = (dp[i-1][0] + dp[i-1][1])%9901

print(sum(dp[n-1])%9901)