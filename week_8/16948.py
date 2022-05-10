# try1 -> 성공, bfs
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
r1,c1,r2,c2 = map(int,input().split())

# 체스판
table = [[0]*n for _ in range(n)]

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]


def bfs(start_x,start_y):
  global r2,c2
  queue = deque([(start_x,start_y)])
  
    
  while queue:
    x,y = queue.popleft()
    # print(x,y)
    if x == r2 and y == c2:
      print(table[x][y])
      return
      
    for i in range(6):
      nx, ny = x+dx[i], y+dy[i]
      if 0<=nx<n and 0<=ny<n and table[nx][ny] == 0:
        table[nx][ny] = table[x][y] + 1        
        queue.append((nx,ny))
  
  print(-1)
  return      


bfs(r1,c1)