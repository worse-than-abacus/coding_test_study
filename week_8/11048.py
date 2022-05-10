#try1 -> 성공
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
table = []
dp = [[0]*(m+1) for _ in range(n+1)]

for _ in range(n):
  row = list(map(int,input().split()))
  table += [row]

dp[0][0]  = table[0][0]

for x in range(n):
  for y in range(m):

    if x+1<n and y<m:
      dp[x+1][y] = max(dp[x][y]+table[x+1][y],dp[x+1][y])
    if x<n and y+1<m:
      dp[x][y+1] = max(dp[x][y]+table[x][y+1],dp[x][y+1])
    if x+1<n and y+1<m:
      dp[x+1][y+1] = max(dp[x][y]+table[x+1][y+1],dp[x+1][y+1])

print(dp[n-1][m-1])