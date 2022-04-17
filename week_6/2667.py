# 모범답안
import sys
input = sys.stdin.readline

n = int(input())
table = []
for _ in range(n):
  row = [point for point in list(map(int,input().rstrip()))]
  table += [row]

  
visited = [[False]*n for _ in range(n)]

# 상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
  global cnt
  visited[x][y] = True
  cnt += 1
  
  for i in range(4):
    nx,ny = x+dx[i],y+dy[i]

    if 0<=nx<n and 0<=ny<n:
      if not visited[nx][ny] and table[nx][ny] == 1:
        dfs(nx,ny)


cnt = 0
house_list = []

for x in range(n):
  for y in range(n):
    if table[x][y] == 1 and not visited[x][y]:
      dfs(x,y)
      house_list += [cnt]
      cnt = 0

house_list.sort()
print(len(house_list))

for house in house_list:
  print(house)



# try 1 -> 실패
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
table = []
for _ in range(n):
  row = [point for point in list(map(int,input().rstrip()))]
  table += [row]

  
visited = [[0]*n for _ in range(n)]

# 상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]



# print(table)
def search(x,y):
  if table[x][y] >0:
    if not visited[x][y]:
      visited[x][y] = True
        
  for move in range(4):
    nx, ny = x+dx[move],y+dy[move]
    if 0<=nx< n and 0<=ny<n:
      search(nx,ny)
            



# for x in range(n):
#   for y in range(n):
#     search(x,y)

search(0,0)
print(visited)
