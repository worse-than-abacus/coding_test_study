# 모범답안

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
m,n = map(int,input().split())
table = []
visited = [[False]*(m) for _ in range(n)]

for _ in range(n):
    row = list(map(int,input().rstrip()))
    # print(row)
    table.append(row)


def bfs():

  queue = deque([(0,0)])
    # 상하좌우
  dx = [0,0,-1,1]  
  dy = [-1,1,0,0]
  visited[0][0] = 1
  

  while queue:
    x,y = queue.popleft()
    
    if x == n-1 and y == m-1:
      return
    # print(x,y)
    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]
        
        if 0 <= next_x < n and 0 <= next_y < m:
          # 방문 안했으면
          if not visited[next_x][next_y]:
            visited[next_x][next_y]= True
            # 다음 지점이 벽이면
            if table[next_x][next_y] == 1: 
              visited[next_x][next_y] = visited[x][y] + 1
              queue.append((next_x,next_y))            
            else:
              # 벽이 없는 길을 최우선순위로
              visited[next_x][next_y] = visited[x][y]
              queue.appendleft((next_x,next_y))            
            
bfs()
print(visited[n-1][m-1]-1)