# 모범코드
import sys
from collections import deque
input = sys.stdin.readline
n= int(input())


def bfs(node):
  visited[node] = 1
  queue = deque([node])
  
  while queue:
    node = queue.popleft()
    for connected_node in graph[node]:
      if not visited[connected_node]: # 연결된 노드, 방문 x라면
        visited[connected_node] = -visited[node]
        queue.append(connected_node)
      else:
        if visited[connected_node] == visited[node]:
          return False      
  return True

for _ in range(n):
  v,e = list(map(int,input().strip().split()))
  graph = {node:list() for node in range(1,v+1)}
  visited = [0] * (v+1)
  isStop = False
  for _ in range(e):
    node_a, node_b =list(map(int,input().strip().split()))
    graph[node_a] += [node_b]
    graph[node_b] += [node_a]

  for node in range(1,v+1):
    if not visited[node]:
      if not bfs(node):
        isStop = True
        break
        
  print('NO' if isStop else 'YES')