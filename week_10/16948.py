from collections import deque

dy = [-2, -2, 0, 0, +2, +2]
dx = [-1, +1, -2, +2, -1, +1]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    visited[y][x] = 0

    while queue:
        y, x = queue.popleft()
        # if curX == c and curY == d:
        #     print(visited[curX][curY] - 1)
        #     return True

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < l and 0 <= nx < l and visited[nx][ny] == -1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))


l = int(input())
visited = [[-1] * l for _ in range(l)]
a, b, c, d = map(int, input().split())
bfs(b, a)
print(visited[c][d])

# fail -> python overtime
# fail2 -> pypy3 out of memory

# Try 2
# different things : list -> tuple
from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == -1:
                q.append((ny, nx))
                graph[ny][nx] = graph[y][x]+1

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
graph = [[-1] * n for _ in range(n)]
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
bfs(r1, c1)

print(graph[r2][c2])