import sys
from collections import deque
input  = sys.stdin.readline

N, M, K = map(int, input().split())

board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)] # False로 하면 시간초과
dx = [1, -1, 0, 0] # 방향순서에 따라서도 시간초과 걸릴 수 있다.
dy = [0, 0, -1, 1]

def bfs(x,y):
    q = deque()
    q.append([x,y,0])
    visited[x][y][0] = 1

    while q:
        x, y, c = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][c]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] and c < K and not visited[nx][ny][c+1]:
                    visited[nx][ny][c + 1] = visited[x][y][c] + 1
                    q.append([nx, ny, c+1])
                elif not board[nx][ny] and not visited[nx][ny][c]:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    q.append([nx, ny, c])
    return -1


print(bfs(0,0))

