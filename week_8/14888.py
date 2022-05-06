# 모범답안, dfs
# 14888번 연산자 끼워 놓기
# dfs 이용

# 수의 개수 입력받기
n = int(input())
# 수열 입력받기
data = list(map(int, input().split()))
# 연산자 개수 계산
add, sub, mul, div = map(int, input().split())

# 최댓값과 최솟값 초기화
max_value = -1e9
min_value = 1e9

# dfs 매서드 정의
def dfs(i, arr):
  global add, sub, mul, div, max_value, min_value
  # 주어진 수열을 다 받았을 경우 최댓값과 최솟값 계산
  if i == n:
    max_value = max(max_value, arr)
    min_value = min(min_value, arr)
  else:
    # 더하기
    if add > 0:
      add -= 1
      dfs(i+1, arr + data[i])
      add += 1
    # 빼기
    if sub > 0:
      sub -= 1
      dfs(i+1, arr - data[i])
      sub += 1
    # 곱하기
    if mul > 0:
      mul -= 1
      dfs(i+1, arr * data[i])
      mul += 1
    # 나누기
    if div > 0:
      div -= 1
      dfs(i+1, int(arr / data[i]))
      div += 1
  
# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 출력
print(max_value)
print(min_value)


# 모범답안 -> 순열과 BFS
# 14888번 연산자 끼워 놓기

# 파이썬에서의 순열 라이브러리 이용
from itertools import permutations
from collections import deque

n = int(input())
seq = list(map(int, input().split()))

# 연산자 
cal = ['+', '-', '*', '//']
# 연산자 입력받기
cal_input = list(map(int, input().split()))
cal_list = []

# 계산할 수 있는 연산자
for i in range(4):
  # 특정 연산자가 존재하지 않는다면 패스
  if cal_input[i] == 0:
    pass
  # 특정 연산자가 존재한다면 그 개수만큼 계산 리스트에 추가
  else:
    for j in range(cal_input[i]):
      cal_list.append(cal[i])

# 만들 수 있는 모든 연산자 배열의 경우의 수
num_case = list(permutations(cal_list, len(cal_list)))
q = deque(num_case)

# 최댓값, 최솟값 초기화
max_result = -1e9
min_result = 1e9

# 큐가 빌 때까지 모든 경우의 수에 대해 연산 수행
while q:
  # 연산자들에 대하여 
  now_list = q.popleft()
  result = seq[0]
  # 차례로 연산 수행
  for i in range(1, len(seq)):
    # 연산자가 더하기라면
    if now_list[i-1] == '+':
      result += seq[i]
    # 연산자가 빼기라면
    elif now_list[i-1] == '-':
      result -= seq[i]
    # 연산자가 곱하기라면
    elif now_list[i-1] == '*':
      result *= seq[i]
    # 연산자가 나누기라면
    else:
      if result < 0:
        result = -(abs(result) // seq[i])
      else:
        result = result // seq[i]    
  # 최댓값, 최솟값 계산      
  max_result = max(max_result, result)
  min_result = min(min_result, result)

# 결과 출력
print(max_result)
print(min_result)










# try1 -> 실패
import sys
from itertools import combinations
from collections import defaultdict

input = sys.stdin.readline


n = int(input())
# +,-,*,/
cal_input = list(map(int,input().split()))

cal_list = defaultdict(int)
for cidx,cal in enumerate(cal_input):
  cal_list[cidx] = cal
  
cals = ["+"]*cal_list[0] + ["-"]*cal_list[1] + ["*"]*cal_list[2] + ["/"]*cal_list[3]
numbers = list(map(int,input().split()))


num_combs = combinations(numbers,len(numbers))
cal_combs = combinations(cals,len(numbers)-1)

max_answer = -10**9
min_answer = 10**9

for num_comb in num_combs:
  num_comb= list(num_comb)
  result = num_comb[0]
  for cal_comb in cal_combs:
    idx = 0
    # comb = list(cal_comb).copy()
    for cal in cal_comb:
      if cal == "+":
        result += num_comb[idx]

      elif cal == "-":
        result -= num_comb[idx]

      elif cal == "*":
        result *= num_comb[idx]
      elif cal == "/":
        result /= num_comb[idx]
      
      idx += 1
      print(cal)
  max_answer = max(max_answer,result)
  min_answer = min(min_answer,result)



print(max_answer)
print(min_answer)

# for cal_comb in cal_combs:
#   print(list(cal_comb))
