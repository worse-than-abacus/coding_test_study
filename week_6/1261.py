import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
table = []
break_wall = [[0]*(n+1) for _ in range(m+1)]
break_wall[0][0] = 0
for _ in range(n):
    row = list(map(int,input().rstrip()))
    # print(row)
    table.append(row)


def dfs(x,y):
    # 상하좌우
  dx = [0,0,-1,1]  
  dy = [-1,1,0,0]
  if x == n and y == m:
    return
    
  for i in range(4):
      next_x, next_y = x+dx[i], y+dy[i]
      if 1 <= next_x <= n and 1 <= next_y <= m:
          if table[next_x][next_y] == 1: # 다음 지점이 벽일 때
              break_wall[next_x][next_y]  = break_wall[x][y] + 1   
          # print(next_x,next_y)        
          else:
            break_wall[next_x][next_y]  = break_wall[x][y]
          dfs(next_x,next_y)
          
            

# for x in range(n):
#     for y in range(m):
#         dfs(x,y)
dfs(1,1)
MIN_NUM = 10**6
for row in break_wall:
    if MIN_NUM > min(row):
        MIN_NUM = min(row)

print(MIN_NUM)
