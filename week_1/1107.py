# try1  -> 예제 1 실패
# 5 기준 거리
import sys
input = sys.stdin.readline

N =[int(n) for n in input().rstrip()]
# print(N)

bnum = int(input())
if bnum == 0:
  brokens = []
else:
  brokens = [int(n) for n in input().split()]

# 5 기준 거리
distance_dict = {
  0 : [5],
  1 : [4,6],
  2 : [3,7],
  3 : [2,8],
  4 : [1,9],
  5 : [0]
}

pushed = []
for num in N:
  distance = abs(num - 5)
  for button in distance_dict[distance]:
    if button not in brokens:
      pushed += [button]
      break

print(pushed)      

# try 2- > 예제 7 실패
# 자리수 기반 거리 구하기
import sys
input = sys.stdin.readline
target = int(input().rstrip())
N =[int(n) for n in str(target)]
bnum = int(input())
if bnum == 0:
  brokens = []
else:
  brokens = [int(n) for n in input().split()]


answer = 0
base_channel = 100

pushed = []
for num in N:
  # 거리 직접 구하기
  MIN = 10
  min_button = 0
  for i in range(0,9+1):
    if i not in brokens:
      distance = abs(num - i)
      
      if MIN > distance: 
        MIN = distance
        min_button = i
  
  pushed += [min_button]
  answer += 1
  
print(pushed)
base_channel = int("".join(list(map(str,pushed))))
answer += abs(target - base_channel)

print(answer)


# try 3 -> 모범답안

# 1. 누를 수 있는 번호 누르기(고장난 버튼 피해서)
# 2. 누른 횟수 = len(str(현재 채널 )) + abs(현재채널 - 목표 채널)
# 3. 최소 비교
# 전체 범위에 대해 1~3 반복

target = int(input())
ans = abs(100 - target) # ++ or -- 로 이동할 경우 -> 최댓값
M = int(input())
if M: # 고장난게 있을 경우만 인풋을 받음
    broken = set(input().split())
else:
    broken = set()

# for ~ else  : break 여부 판단 (break 없이 빠져나오면 else 실행)
# 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
for num in range(1000001): 
    for N in str(num):
        if N in broken: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            break
    else: # 고장이 안 났다면
      # 번호를 눌러서 만들 수 있는 경우라면
      # min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)