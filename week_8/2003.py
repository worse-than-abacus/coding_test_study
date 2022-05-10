# trt2 -> 성공, 투포인터
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
numbers = list(map(int,input().split()))

answer = 0
start, end = 0, 1

while start <= end and end <= n:
  cur_sum = sum(numbers[start:end])
  
  if cur_sum == m :
    answer += 1
    end += 1
    
  elif cur_sum < m :
    end += 1
  else:
    start+=1  

print(answer)

# try1 -> 시간 초과
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
numbers = list(map(int,input().split()))

answer = 0
for i in range(n-1):
  cur_sum = 0
  j = i
  while cur_sum < m and j < n:
    cur_sum += numbers[j]
    j += 1
    # print(j,cur_sum)

  if cur_sum == m:
    answer += 1
  

print(answer)

