from itertools import combinations

n = int(input())
power =[list(map(int,input().split())) for _ in range(n)]
members =list(range(n))
team_list = list(combinations(members,n//2))

gap = 10000
for i in range(len(team_list)//2):
  team_a = team_list[i]
  team_b = team_list[-i-1]
  a_power = 0
  b_power = 0
  
  for j in range(n//2):
    member = team_a[j]
    for other_member in team_a:
      a_power += power[member][other_member]
      
  for j in range(n//2):
    member = team_b[j]
    for other_member in team_b:
      b_power += power[member][other_member]

  gap = min(gap, abs(a_power - b_power))

print(gap)