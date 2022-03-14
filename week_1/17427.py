# try1 -> 시간 초과
import sys
input = sys.stdin.readline

def sumDiv(y):
  sum_div = 0  # sum(약수)
  for i in range(1,y+1):
    if y%i == 0: #약수이면
      sum_div += i
  return sum_div

N = int(input())
answer = 0
for num in range(1,N+1):
  answer += sumDiv(num)
print(answer)

# try2
import sys
input = sys.stdin.readline

N = int(input())
answer = 0
for num in range(1,N+1):
  # (N//num):num이 N에 들어가는 개수
  # 30//4 = 7 : 30에 4가 7번 들어감
  # num이 포함되는 횟수 * num = [1,N]의 모든 num의 합
  answer += (N//num)*num
print(answer)