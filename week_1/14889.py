# try1 -> 시간 초과

import sys
from itertools import combinations,permutations

input = sys.stdin.readline

n = int(input())
table = []
table_sum = 0
for i in range(n):
  row = list(map(int,input().split()))
  table += [row]
  table_sum += sum(row)

MIN = 10e-6
players = [n for n in range(1,n+1)]

for teamA in permutations(players,int(n/2)):
  sumA, sumB = 0, 0
  teamB = set(players) - set(teamA)
  for x,y in permutations(teamA,2):
    sumA += table[x-1][y-1]

  for x,y in permutations(teamB,2):
    sumB += table[x-1][y-1]

  diff = int(abs(sumA-sumB))
  if MIN > diff:
    MIN =  diff

print(MIN)

# try 2 모범답안
from itertools import combinations #조합 함수

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = []

#조합으로 가능한 팀 생성해주기
for team in list(combinations(members, N//2)):
    possible_team.append(team)

min_stat_gap = 10000 #갭이 가장 작은 값을 찾기 위하여
for i in range(len(possible_team)//2):
    #A 팀
    team = possible_team[i]
    stat_A = 0 #A팀 능력치
    for j in range(N//2):
        member = team[j] #멤버
        for k in team:
            stat_A += S[member][k] #멤버와 함께할 경우의 능력치들
            
    #A를 제외한 나머지 팀
    team = possible_team[-i-1]
    stat_B = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]
            
    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))
    
print(min_stat_gap)

# try3 


import sys
from itertools import combinations,permutations

input = sys.stdin.readline

n = int(input())
table = []
table_sum = 0
for i in range(n):
  row = list(map(int,input().split()))
  table += [row]
  table_sum += sum(row)

MIN = 10e-6
players = [n for n in range(1,n+1)]

for teamA in range(players,int(n/2)):
  sumA, sumB = 0, 0
  teamB = set(players) - set(teamA)
  for x,y in range(int(n/2)):
    sumA += table[x-1][y-1]

  for x,y in  range(int(n/2)):
    sumB += table[x-1][y-1]

  diff = int(abs(sumA-sumB))
  if MIN > diff:
    MIN =  diff

print(MIN)
