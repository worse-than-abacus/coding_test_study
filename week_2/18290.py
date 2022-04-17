# try 1 -> 실패..
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
table = []

for _ in range(n):
  row = list(map(int,input().split()))
  table += [row]

selected = []
visited = [[0]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(node,cnt,sum_value):
    x,y = node

    if cnt == k:
        global max_value
        max_value = max(max_value, sum_value)
        return

    for row in range(x,n):
        for col in range(y,m):
            if not visited[row][col]:
                for i in range(4):
                    nx, ny = row + dx[i], col + dy[j]
                    if 0 <= nx < n and 0<= ny < m:
                        break
                else:
                    visited[row][col] = True
                    dfs((i,j),cnt+1, sum_value+table[row][col])
                    visited[row][col] = False
    
  
# try2 -> 모범 코드
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = -1000000

def go(px, py, index, sum):
    if index == k:
        global answer
    
        if answer < sum:
            answer = sum
        
        return

    for x in range(px, n):
        for y in range(py if x==px else 0, m):
            # 현재 위치 방문했었는지 확인
            if visited[x][y]:
                continue

            ok = True
            # 동서남북 방문 했었는지 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny]:
                        ok = False            
            # 방문
            if ok:
                visited[x][y] = True
                go(x, y, index+1, sum+arr[x][y])
                visited[x][y] = False


go(0, 0, 0, 0)

print(answer)
