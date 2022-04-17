# 모범답안
import sys
from collections import deque

input = sys.stdin.readline
n,m,v = list(map(int,input().split()))

table = [[False]*(n+1) for _ in range(n+1)]

for _ in range(m):
  nodeA, nodeB = list(map(int,input().split()))
  table[nodeA][nodeB] = True
  table[nodeB][nodeA] = True


def dfs(start_node):
  print(start_node,end=" ")
  visited[start_node] = True

  for node in range(1, n+1):
    if table[start_node][node]:
      if not visited[node]:
        dfs(node)


def bfs(start_node):
  queue = deque([start_node])
  visited[start_node] = True

  while queue:
    start_node = queue.popleft()
    print(start_node, end=" ")

    for node in range(1, n+1):
      if table[start_node][node]:
        if not visited[node]:
          queue.append(node)
          visited[node] = True


visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)

