# 모범답안
n = int(input())
lst = list(map(int, input().split()))

dp = [1 for i in range(n)]
array = [[x] for x in lst]

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j] and dp[j] + 1 > dp[i]:
          array[i] = array[j] + [lst[i]]
          dp[i] = dp[j] + 1
          
length = 0
flag = 0
for i in range(n):
    if length < dp[i]:
        flag = i
        length = dp[i]
print(length)
print(*array[flag])

# try 7 실패
import sys
input = sys.stdin.readline
n = int(input())
cost = list(map(int,input().split()))
dp = [0]*(1000+1)

MAX_LENGTH = -1
answer_list = []

for i in range(n):
  row_list = []
  for j in range(i):
    if dp[i] <= dp[j] and cost[i] > cost[j]:
      row_list.append(cost[j])
      dp[i] = dp[j]
  dp[i] += 1
  row_list.append(cost[i])
  if MAX_LENGTH < dp[i]:
    MAX_LENGTH = dp[i]
    answer_list = row_list.copy()

print(MAX_LENGTH)
print(*answer_list)


# try 1 ~ 6  , 실패
import sys
input = sys.stdin.readline
n = int(input())
cost = list(map(int,input().split()))
dp = [1]*(1000+1)

MAX_LENGTH = -1
answer_list = []

for i in range(n):
  row_list = []
  for j in range(i):
    if dp[i] <= dp[j] and cost[i] > cost[j]:
      dp[i] = dp[j] + 1
      row_list.append(cost[j])
  row_list.append(cost[i])
  if MAX_LENGTH <= dp[i]:
    MAX_LENGTH = dp[i]
    answer_list = row_list.copy()

print(MAX_LENGTH)
print(*answer_list)
