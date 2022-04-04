###################컴비네이션
from itertools import combinations
N, M = map(int,input().split())
arr=list(range(1,N+1))
for e in list(combinations(arr, M)):  
    print(*e)




###################
N, M = map(int,input().split())
s =[] #출력대상
def dfs(start):
    if len(s)==M :
        print(*s)
        return
    for i in range(start,N+1):
        s.append(i)
        dfs(i+1)
        s.pop()
dfs(1)