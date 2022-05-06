# 모범답안 -> combination
from itertools import combinations

visited =  [0]*2000001

visited[0] = 1

n = int(input())
data =  list(map(int, input().split()))

for i in range(1, n+1): # n번 돌면서   

    for comb in combinations(data, i): # i개 뽑아내는 조합을 가져온다.

        visited[sum(comb)] = 1
    
print(visited.index(0))

# 모범답안 -> dfs
n = int(input()) 
num = list(map(int,input().split())) 

visited = [0]*10000000 

def dfs(idx,sum) : 
    if idx == n : 
        return 
    sum += num[idx] 
    visited[sum] = 1 
    dfs(idx+1, sum) 
    dfs(idx+1, sum-num[idx]) 

dfs(0,0) 
print(visited[1:].index(0)+1)



# 내 풀이 -> 시간초과
import sys
from collections import defaultdict
input = sys.stdin.readline

visited = defaultdict(int)
n = int(input())
s =  list(map(int,input().split()))
# s.sort()


numSum = 0

def addNum(numSum, curNums):
  if len(curNums) == 0:
    return
  
  
  for num in curNums:
    nextNums = curNums.copy()
    nextNums.remove(num)
    
    if not visited[numSum+num]:
      numSum += num
      visited[numSum] = True

      addNum(numSum,nextNums)
      numSum -= num
    else:
      addNum(numSum,nextNums)
    
addNum(numSum,s)

MAXNUM = 100_000
for i in range(1,MAXNUM+1):
  if not visited[i]:
    print(i)
    break