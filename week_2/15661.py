## try1 time-out
from itertools import combinations


n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]
members = list(range(n))
gap =10000

team_list = []
for i in range(1,n):
  team_list.extend(list(combinations(members,i)))

gap = 10000
for i in range(len(team_list)//2):
  team_a = team_list[i]
  team_b = team_list[-i-1]
  a_power = 0
  b_power = 0
  
  for j in range(len(team_a)):
    member = team_a[j]
    for other_member in team_a:
      a_power += power[member][other_member]
      
  for j in range(len(team_b)):
    member = team_b[j]
    for other_member in team_b:
      b_power += power[member][other_member]

  gap = min(gap, abs(a_power - b_power))

print(gap)

## try2 time-out

from itertools import combinations ,permutations
import sys

n = int(sys.stdin.readline())
power = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
members = list(range(n))


gap = 10000

team_list = []
for i in range(1,n):
  team_list.extend(list(combinations(members,i)))

gap=10000
for i in range(len(team_list)//2):
  team_a = team_list[i]
  team_b = team_list[-i-1]
  team_a_index = list(permutations(team_a,2))
  team_b_index = list(permutations(team_b,2))
  a_power = 0
  b_power = 0

  for j,k in team_a_index:
    a_power += power[j][k]

  for j,k in team_b_index:
    b_power += power[j][k]

  gap = min(gap,abs(a_power - b_power))

print(gap)