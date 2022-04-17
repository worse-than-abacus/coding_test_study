# 모범답안

import sys
input = sys.stdin.readline
T = int(input())
MAXLIMIT= 100001
MOD = 1000000009
dp=[[0 for _ in range(3)] for i in range(MAXLIMIT)]

# dp[i]가 되는 모든 경우의 수를 마지막에 오는 숫자에 따라 분류 
# [# of 1, # of 2, # of 3]        
dp[1]=[1,0,0]
dp[2]=[0,1,0]
dp[3]=[1,1,1] 
# 3을 1,2,3의 합으로 나타낼 수 있는 경우의 수 : 3
# 끝이 1로 끝나는 경우 1 : 1 + 2 + 1
# 끝이 2로 끝나는 경우 1 : 1 + 2
# 끝이 3로 끝나는 경우 1 : 3

for i in range(4,MAXLIMIT):    
    dp[i][0]=dp[i-1][1]%MOD+dp[i-1][2]%MOD
    dp[i][1]=dp[i-2][0]%MOD+dp[i-2][2]%MOD
    dp[i][2]=dp[i-3][0]%MOD+dp[i-3][1]%MOD

for i in range(T):
    n=int(input())
    print(sum(dp[n]) % MOD)
