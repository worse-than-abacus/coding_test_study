# 오늘의 뇌 깨우기 BFS 답지 보고 문제풀기
import copy 
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
ans = 0
queue = deque()

def bfs():
    global ans
    copy_map = copy.deepcopy(map)
    for i in range(m):
        for j in range(n):
            if copy_map[i][j] == 2:
                queue.append([i,j])

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0<= ny < m :
                if copy_map[nx][ny] == 0:
                    copy_map[nx][ny] = 2
                    queue.append([nx, ny])

    cnt = 0
    for i in copy_map:
        cnt += i.count(0)
    ans = max(ans, cnt)

def make_wall(CNT):
    if CNT == 3:
        bfs()
        return
    for a in range(n):
        for b in range(m):
            if map[a][b] == 0:
                map[a][b] = 1
                make_wall(CNT+1)
                map[a][b] = 0

make_wall(0)
print(ans) 
# pypy3 로 해야 풀린다.
