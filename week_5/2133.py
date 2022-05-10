# try 10 -> 실패
import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*(30+1)
dp[2] = 3
dp[4] = dp[2]*dp[2]+2
dp[6] = dp[4]*dp[2] +2
for i in range(7,n+1):
  if i % 6 ==  0:
    dp[i] = dp[i-6]*dp[6]
  elif i % 4 ==  0:
    dp[i] = dp[i-4]*dp[4]
  elif i % 2 == 0:
    dp[i] = dp[i-2]*dp[2]

print(dp[n])
# try 7,8,9 -> 실패
# 추가: 2와 4의 배수가 아니면
# dp[i] = dp[i-1] +1
# dp[i] = dp[i-1] +2
# dp[i] = dp[i-1]*2
import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*(30+1)
dp[2] = 3
dp[4] = 8
for i in range(5,n+1):
  if i % 4 ==  0:
    dp[i] = dp[i-4]*8
  elif i % 2 == 0:
    dp[i] = dp[i-2]*3
  else:
    dp[i] = dp[i-1]*2

print(dp[n])

# try 6 -> 실패
# 추가: 2와 4의 배수가 아니면, dp[i] = dp[i-1] 
import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*(30+1)
dp[2] = 3
dp[4] = 8
for i in range(5,n+1):
  if i % 4 ==  0:
    dp[i] = dp[i-4]*8
  elif i % 2 == 0:
    dp[i] = dp[i-2]*3
  else:
    dp[i] = dp[i-1]


# try 5 -> 실패
# range(4,n+1) -> range(5,n+1)
import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*(30+1)
dp[2] = 3
dp[4] = 8
for i in range(5,n+1):
  dp[i] = dp[i-2]*3 + dp[i-4]*2
    
print(dp[n])

# try 4 -> 실패
# range(4,n+1) -> range(5,n+1)
import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*(30+1)
dp[2] = 3
dp[4] = 8
for i in range(5,n+1):
  if i % 4 ==  0:
    dp[i] = dp[i-4]*8
  elif i % 2 == 0:
    dp[i] = dp[i-2]*3

print(dp[n])


# try 3 -> 실패
import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*(30+1)
dp[2] = 3
dp[4] = 8
for i in range(4,n+1):
  dp[i] = dp[i-2]*3 + dp[i-4]*2
    
print(dp[n])

# try 2 -> 실패
import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*(30+1)
dp[2] = 3
dp[4] = 8
for i in range(4,n+1):
  if i % 4 ==  0:
    dp[i] = dp[i-4]*8
  elif i % 2 == 0:
    dp[i] = dp[i-2]*3

print(dp[n])

# try 1 -> 실패
import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*(30+1)
dp[2] = 3
dp[4] = 8
for i in range(4,n+1):
  if i % 4 ==  0:
    dp[i] = dp[i-4]*8
  elif i % 2 == 0:
    dp[i] = dp[i-2]*3

print(max(dp[:n+1]))