import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = [[] for _ in range(n)]
visited = [False] * n
result = False

for _ in range(m):
  a, b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)

def dfs(depth, x):
  global result
  if depth == 4:
    result = True
    return

  for i in arr[x]:
    if not visited[i]:
      visited[i] = True
      dfs(depth+1,i)
      visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(0, i)
    visited[i] = False
    if result:
        break

print(1 if result else 0)