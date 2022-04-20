

# try 3 -> 성공
## 종료조건 변경 : visited의 길이
### visited를 table에서 list로 변경, cnt 제거

import sys
input = sys.stdin.readline


n,m = list(map(int,input().split()))
graph = {node:list() for node in range(n)}
# visited = [[False]*n for _ in range(n)]
visited = []
for _ in range(m):
  node_a, node_b = list(map(int,input().split()))

  # 맵이 2차원 형태로 주어지지 않았기 때문에
  ## 빠른 연산을 위한 인접행렬 방식 선택
  graph[node_a] += [node_b]
  graph[node_b] += [node_a]

# print(graph)
def dfs(start_node):
  global cnt, isStop


  if len(visited)>4:
    isStop = True
    print(1)
    return
  
  
  for next_node in graph[start_node]:
    if next_node not in visited:
      # print(visited)
      visited.append(next_node)
      dfs(next_node)  
      visited.pop()
      
    if isStop:
      return True
    
isStop = False
for start_node in range(n):
  
  dfs(start_node)
  if isStop:
    break
else:
  print(0)



# try 2-> 실패, 12%
# cnt =0 -> cnt -=1
import sys
input = sys.stdin.readline


n,m = list(map(int,input().split()))
graph = {node:list() for node in range(n)}
visited = [[False]*n for _ in range(n)]
for _ in range(m):
  node_a, node_b = list(map(int,input().split()))
  graph[node_a] += [node_b]
  graph[node_b] += [node_a]

# print(graph)
def dfs(start_node):
  global cnt, isStop
  cnt += 1

  if cnt > 4:
    isStop = True
    print(1)
    return
  
  
  for next_node in graph[start_node]:
    if not visited[start_node][next_node]:
      # print("cnt = ", cnt,"!!" ,start_node,"->",next_node)
      visited[start_node][next_node] = True
      visited[next_node][start_node] = True
      dfs(next_node)  
      visited[start_node][next_node] = False
      visited[next_node][start_node] = False
      cnt -= 1
    if isStop:
      return True
    
isStop = False
for start_node in range(n):
  cnt = 0
  dfs(start_node)
  if isStop:
    break
else:
  print(0)

# try 1 -> 실패, 8%
import sys
input = sys.stdin.readline


n,m = list(map(int,input().split()))
graph = {node:list() for node in range(n)}
visited = [[False]*n for _ in range(n)]
for _ in range(m):
  node_a, node_b = list(map(int,input().split()))
  graph[node_a] += [node_b]
  graph[node_b] += [node_a]

# print(graph)
def dfs(start_node):
  global cnt, isStop
  cnt += 1

  if cnt > 4:
    isStop = True
    print(1)
    return
  
  
  for next_node in graph[start_node]:
    if not visited[start_node][next_node]:
      # print("cnt = ", cnt,"!!" ,start_node,"->",next_node)
      visited[start_node][next_node] = True
      visited[next_node][start_node] = True
      dfs(next_node)  
      visited[start_node][next_node] = False
      visited[next_node][start_node] = False
      cnt = 0
    if isStop:
      return True
    
isStop = False
for start_node in range(n):
  cnt = 0
  dfs(start_node)
  if isStop:
    break
else:
  print(0)