###########퍼뮤테이션
from itertools import permutations

N, M = map(int, input().split())
arr = list(range(1, N+1))

for e in list(permutations(arr, M)):
  print(*e)


###################################
N, M = map(int, input().split())
s=[] # 출력 대상

def dfs() :
  if len(s)==M : 
    print(*s)
    return
  for i in range(1,N+1):
    if i in s :
      continue
    s.append(i)
    dfs()
    s.pop()

dfs()   