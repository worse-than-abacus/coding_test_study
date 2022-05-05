import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

queue = deque()

def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(6):
            nx, ny = x+dx[k], y+dy[k]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and board[nx][ny]==0:
                queue.append((nx, ny))
                board[nx][ny] = board[x][y] + 1
queue.append((r1,c1))

bfs()
print(board[r2][c2] if board[r2][c2] else -1)

