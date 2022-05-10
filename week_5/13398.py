# 모범답안
import sys

input = sys.stdin.readline

N = int(input())
input_array = list(map(int, input().split()))
dp = [[x for x in input_array] for _ in range(2)]

for i in range(1, N):
  # 일반적인 최대값 : dp[0][i]
    dp[0][i] = max(dp[0][i - 1] + input_array[i], dp[0][i])
  # 제거한 경우의 최대값 : dp[1][i]
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + input_array[i])
  ## i번째 원소를 제거한 경우
  ### dp[0][i - 1] : i번째 원소를 더하지 않음 = 제거한 것과 같은 의미
  ### dp[0][i]- input_array[i]
  
  ## dp[1][i - 1] + input_array[i] : 특정 원소를 제거한 경우의 최댓값 + i번째 원소

print(max(max(dp[0]), max(dp[1])))



# try1 -> 시간 초과
import sys

input = sys.stdin.readline

n = int(input())
sequences = list(map(int,input().split()))
minus_sequences = [(-1,0)]

for minus_idx, num in enumerate(sequences):
  if num < 0:
    minus_sequences += [(minus_idx,num)]

dp = [0] * n
dp[0] = max(sequences[0],0)


for i in range(1,n):
  for j in range(i):
    dp[i] = dp[i-1]+sequences[i]


answer = -1001
for i in range(n):
  for minus_idx, minus_num in minus_sequences:
    if minus_idx <= i:
      answer = max(answer,dp[i]-minus_num)

print(answer)