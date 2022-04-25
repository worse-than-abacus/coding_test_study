# 모범답안
n, m = map(int, input().split(' '))
r, c, d = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(x, y, d):
    global count

    dir = d
    for i in range(4):
        dir = (dir + 3) % 4

        new_x = x + dx[dir]
        new_y = y + dy[dir]

        # 범위를 벗어날 경우
        if new_x < 1 or new_x > n or new_y < 1 or new_y > m:
            continue

        # 벽일 경우
        if maps[new_x][new_y] == 1:
            continue

        # 청소를 안한 영역일 경우
        if maps[new_x][new_y] == 0:
            maps[new_x][new_y] = 2
            count += 1
            go(new_x, new_y, dir)
            return

    # 여기로 코드가 넘어온 경우는 
    # 청소를 하면서 넘어온 경우에 더이상 나아갈 방향이 없는 경우
    dir = (dir + 2) % 4
    new_x = x + dx[dir]
    new_y = y + dy[dir]
    
    # 후진을 하려는데 벽인 경우
    if maps[new_x][new_y] == 1:
        return
    else:
        go(new_x, new_y, d)

count = 1
maps[r][c] = 2
go(r, c, d)
print(count)

# try1 -> 실패
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
r,c,d = map(int,input().split())

table = []
visited = []
for _ in range(n):
  row = list(map(int,input().split()))
  table += [row.copy()]
  visited += [row.copy()]


dx = deque([-1,0,1,0])
dy = deque([0,1,0,-1])



visited[r][c] = 1
cnt = 1
isStop = False
# dfs
def move(start_x,start_y,dir):
  global cnt,visited, table, dx, dy, isStop
  if isStop:
    return
  
  for i in range(dir,dir+4):
    i = int(i%4)
    next_x, next_y = start_x+dx[i], start_y+dy[i]
    if 0<=next_x<n and 0<=next_y<m:
      if not visited[next_x][next_y]:
        cnt += 1
        visited[next_x][next_y] = cnt
        move(next_x,next_y,i)


  next_x, next_y = start_x-dx[dir], start_y-dy[dir]
  if not table[next_x][next_y]:
    move(next_x,next_y,i)
  else:
    isStop = True
    
    cnt -= 1
    return
  
move(r,c,d)
answer = -1
for row in visited:
  answer = max(answer,max(row))

print(answer)