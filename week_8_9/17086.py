import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우/대각선
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if not board[nx][ny]:
                queue.append((nx, ny))
                board[nx][ny] = board[x][y] + 1
for i in range(N):
    for j in range(M):
        if board[i][j]:
            queue.append((i,j))
bfs()
print(max(map(max,board))-1)
