# try1


import sys
input = sys.stdin.readline
E,S,M = list(map(int,input().split()))

# E, S, M 에서 1을 빼면 % 15, %28, %19

year = 0
isSearch = True
while isSearch:
  if E-1 == (year%15):
    if S-1 == (year%28):
      if M-1 == (year%19):
        print(year+1)
        isSearch = False
  year += 1


# 공덕에서 진행됨 (둘다)
  # 4/1 리허설  13:30 ~ 17:00
  # 4/2 최종 발표 # 9시 ~
  # (+공덕반) 1팀당 30분 = 발표 타이머 20분 + 10분 피드백 시간