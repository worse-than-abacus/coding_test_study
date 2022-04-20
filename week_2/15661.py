# trt 1-> pypy3 성공
import sys
from itertools import combinations, product
input = sys.stdin.readline

n = int(input())

table = [list(map(int,input().split())) for _ in range(n)]

total_member = set([member for member in range(n)])

teamA = []
answer = 100000
for i in range(n//2+1):
  for teamA in combinations(total_member,i):
    teamB = set(total_member) - set(teamA)

    teamA_stat,teamB_stat = 0,0
    for playerA,playerB in product(teamA,repeat=2):
      teamA_stat += table[playerA][playerB]
    
    for playerA,playerB in product(teamB,repeat=2):
      teamB_stat += table[playerA][playerB]

    answer = min(answer, int(abs(teamA_stat-teamB_stat)))

print(answer)


# 모범 코드... 하지만 시간초과 , 재귀
import sys

input = sys.stdin.readline

n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]

visited1 = [False] * n

min_value = 100*20

def recur(target):

    if target == n:
        score()
        return


    visited1[target] = True
    recur(target+1)
    visited1[target] = False
    recur(target+1)
            
    

def score():
    global min_value

    start = 0
    link = 0

    for i in range(n-1):
        for j in range(i+1,n):
            if visited1[i] and visited1[j] :
                start += matrix[i][j] + matrix[j][i]
            elif not visited1[i] and not visited1[j]:
                link += matrix[i][j] + matrix[j][i]
    
    diff = abs(start-link)

    if  min_value > diff:
        min_value = diff



recur(0)

print(min_value)

