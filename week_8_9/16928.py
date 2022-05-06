import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board_cnt = [0] * 101
visited = [False] * 101

# 주사위를 계속굴려서 모든 방문가짓수를 찾고 최소 주사위 굴린수를 구한다

ladder = dict()
snake = dict()

for _ in range(N):
    i, j = map(int, input().split())
    ladder[i] = j
for _ in range(M):
    i, j = map(int, input().split())
    snake[i] = j

def bfs():
    queue = deque([1])
    visited[1] = True
    while queue:
        cur = queue.popleft()
        for dice in range(1,7):
           nxt = cur + dice
           if 0 < nxt <= 100 and not visited[nxt]:
               if nxt in ladder.keys():
                   nxt = ladder[nxt]
               if nxt in snake.keys():
                   nxt = snake[nxt]
               if not visited[nxt]:
                   queue.append(nxt)
                   visited[nxt] = True
                   board_cnt[nxt] = board_cnt[cur] + 1
bfs()
print(board_cnt[100])


