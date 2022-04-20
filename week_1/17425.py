
# try1 -> 시간초과
# 17427 번의 코드 * 복수 인풋
import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
  n = int(input())
  answer = 0
  for num in range(1,n+1):
    answer += (n//num)*num
  print(answer)


# try2 -> 시간 초과
# 에라토스테네스의 체... 적용법이 잘못된듯 싶다. 계산량 감소에 영향 X
import sys
input = sys.stdin.readline

T = int(input())

table = [False]*10001
table[0], table[1] = True, True

for num in range(2,10000+1):
  if table[num] == False:
    table[num] = True
    for check in range(num*2,10000+1,num):
      table[check] = False
    
    
for _ in range(T):
  N = int(input())
  answer = 0
  for num in range(1,N+1):
    if table[num]:
      answer += (N//num)*num
  print(answer)



# try 3 -> pypy3 성공 / python3 시간초과
import sys
input = sys.stdin.readline

T = int(input())

table = [1]*1000001
 
 
# 약수의 합 미리 계산하기
for num in range(2,1000000+1):
  # num의 배수에 num 더하기
  # num은 모든 num의 배수의 약수
  for check in range(num,1000000+1,num):
    table[check] += num


cumsum = [0] * 1000001 # 누적합


# 누적합 미리 계산하기
for num in range(1,1000000+1):
  cumsum[num] = cumsum[num-1] + table[num]

for _ in range(T):
  print(cumsum[int(input())])


# try 4 -> pypy3 성공 / python3 시간초과
# 문제 최대 범위가 아닌, 입력 값의 최대값만큼 계산
import sys
input = sys.stdin.readline

T = int(input())
numbers = []
for _ in range(T):
    number = int(input())
    numbers += [number]

# 입력값의 최댓값 저장
MAXNUM = max(numbers)
# MAXNUM = 1000001


# 약수의 합 미리 계산하기
table = [1]*(MAXNUM+1)
for num in range(2,MAXNUM+1):
  # num의 배수에 num 더하기
  # num은 모든 num의 배수의 약수
  for check in range(num,MAXNUM+1,num):
    table[check] += num


# 누적합 미리 계산하기
cumsum = [0] * (MAXNUM+1)
for num in range(1,MAXNUM+1):
  cumsum[num] = cumsum[num-1] + table[num]

for number in numbers:
    print(cumsum[number])