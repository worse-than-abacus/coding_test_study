# 모범답안
import sys
from collections import deque
input = sys.stdin.readline

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        # move[next_point] = x 이기 때문에 before_point(==x)가 저장되어 있음
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x


        for next_point in (x+1, x-1, 2*x): # 방문 순서 바꿔도 동일 왜냐하면

            # next_point에 먼저 방문 == 최단거리
            if 0<=next_point<= MAX_RANGE and dist[next_point]==0: 
                queue.append(next_point)
                dist[next_point] = dist[x] + 1
                move[next_point] = x

N, K = map(int, input().split())
MAX_RANGE = 100000
dist = [0]*(MAX_RANGE+1)
move = [0]*(MAX_RANGE+1)
bfs()


# try1
import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

MAX_RANGE = 100_000
visited = [0] * (MAX_RANGE+1)

def bfs(node):
  queue = deque([node])

  while queue:
    x = queue.popleft()
    print(x)
    if x == k:
      return

    if x*2 <= MAX_RANGE and not visited[x*2]:
      visited[x*2] = visited[x] + 1
      queue.append(x*2)

    if x+1 <= MAX_RANGE and not visited[x+1]:
      visited[x+1] = visited[x] + 1
      queue.append(x+1)

    if x-1 <= MAX_RANGE and not visited[x-1]:
      visited[x-1] = visited[x] - 1
      queue.append(x-1)

bfs(n)
print(visited[k])